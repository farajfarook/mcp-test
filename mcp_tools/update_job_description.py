from typing import Dict, Any
from mcp.server.fastmcp import FastMCP
from pgdb import execute_query


def register_update_job_description(mcp: FastMCP):
    """Register update_job_description tool with the MCP server"""

    @mcp.tool()
    def update_job_description(job_id: int, new_description: str) -> Dict[str, Any]:
        """
        Updates the description for a specific job.

        Args:
            job_id: The ID of the job to update.
            new_description: The new description text for the job.

        Returns:
            A dictionary indicating success or failure.
        """
        query = """
        UPDATE jobs
        SET description = %s
        WHERE id = %s
        RETURNING id;
        """
        try:
            result = execute_query(query, (new_description, job_id))
            if result:
                print(f"Successfully updated description for job ID {job_id}")
                return {"success": True, "job_id": job_id}
            else:
                print(f"Job with ID {job_id} not found for update.")
                return {"success": False, "error": f"Job with ID {job_id} not found"}
        except Exception as e:
            print(
                f"An error occurred while updating job description for ID {job_id}: {e}"
            )
            return {"success": False, "error": str(e)}
