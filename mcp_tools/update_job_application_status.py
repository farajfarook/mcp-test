from mcp.server.fastmcp import FastMCP
from pgdb import execute_query, fetch_one
from typing import Dict, Any


def register_update_job_application_status(mcp: FastMCP):
    """Register update_job_application_status tool with the MCP server"""

    @mcp.tool()
    def update_job_application_status(
        application_id: int, new_status: str
    ) -> Dict[str, Any]:
        """
        Updates the status of a job application.

        Args:
            application_id: ID of the job application to update
            new_status: New status to set for the application (must be one of the valid statuses)

        Returns:
            A dictionary containing the result of the operation
        """
        try:
            # First check if the application exists
            check_query = "SELECT id FROM job_applications WHERE id = %s"
            application = fetch_one(check_query, (application_id,))

            if not application:
                error_message = f"No job application found with ID {application_id}"
                print(error_message)
                return {"success": False, "message": error_message}

            # Validate the new status
            validate_query = "SELECT %s::application_status"
            try:
                fetch_one(validate_query, (new_status,))
            except Exception as e:
                error_message = f"Invalid status '{new_status}'. Status must be one of the valid application statuses."
                print(error_message)
                return {"success": False, "message": error_message}

            # Update the application status
            update_query = """
            UPDATE job_applications 
            SET status = %s::application_status
            WHERE id = %s
            RETURNING id, status, last_updated
            """

            result = fetch_one(update_query, (new_status, application_id))

            if result:
                success_message = (
                    f"Application ID {application_id} status updated to '{new_status}'"
                )
                print(success_message)
                return {
                    "success": True,
                    "message": success_message,
                    "application_id": result[0],
                    "new_status": result[1],
                    "last_updated": result[2].isoformat() if result[2] else None,
                }
            else:
                error_message = (
                    f"Failed to update application status for ID {application_id}"
                )
                print(error_message)
                return {"success": False, "message": error_message}

        except Exception as e:
            error_message = f"An error occurred while updating application status: {e}"
            print(error_message)
            return {"success": False, "message": error_message}
