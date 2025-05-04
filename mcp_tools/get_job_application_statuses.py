from mcp.server.fastmcp import FastMCP
from pgdb import fetch_all


def register_get_job_application_statuses(mcp: FastMCP):
    """Register get_job_application_statuses tool with the MCP server"""

    @mcp.tool()
    def get_job_application_statuses() -> list[str]:
        """
        Fetches all valid statuses for job applications from the database.
        Returns a list of possible application status values.
        """
        fetch_statuses_query = "SELECT enum_range(NULL::application_status);"
        try:
            results = fetch_all(fetch_statuses_query)
            # The query returns a single row with an array of values
            # We need to extract the actual values from the PostgreSQL array
            if results and len(results) > 0:
                # Convert from tuple to a clean list of strings
                statuses = list(results[0][0])
                print("Application statuses:", statuses)
                return statuses
            return []
        except Exception as e:
            print(f"An error occurred while fetching application statuses: {e}")
            return []
