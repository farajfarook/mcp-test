from mcp.server.fastmcp import FastMCP
from pgdb import fetch_all


def register_get_all_candidate_names(mcp: FastMCP):
    """Register get_all_candidate_names tool with the MCP server"""

    @mcp.tool()
    def get_all_candidate_names() -> list[str]:
        """
        Fetches all candidate names from the database.
        """
        fetch_all_query = "SELECT name FROM candidates"
        try:
            results = fetch_all(fetch_all_query)
            print("Candidate names:", results)
            return results
        except Exception as e:
            print(f"An error occurred while fetching candidate names: {e}")
            return []
