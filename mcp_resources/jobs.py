from typing import Any, Dict, List
from mcp.server.fastmcp import FastMCP
from pgdb import fetch_all


def register_jobs_resource(mcp: FastMCP):
    """Register jobs resource with the MCP server"""

    @mcp.resource("resource://jobs")
    def get_jobs() -> List[Dict[str, Any]]:
        """
        Resource endpoint that fetches all jobs from the database.

        Returns:
            A list of dictionaries containing job details (id, title, description)
        """
        query = """
        SELECT 
            id, 
            title, 
            description, 
            created_at
        FROM jobs
        ORDER BY created_at DESC
        """

        try:
            results = fetch_all(query)

            jobs = []
            for row in results:
                jobs.append(
                    {
                        "id": row[0],
                        "title": row[1],
                        "description": row[2],
                        "created_at": row[3].isoformat() if row[3] else None,
                    }
                )

            print(f"Found {len(jobs)} jobs")
            return jobs

        except Exception as e:
            print(f"An error occurred while fetching jobs: {e}")
            return []
