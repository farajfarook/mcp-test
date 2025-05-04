from typing import Any, Dict, List
from mcp.server.fastmcp import FastMCP
from pgdb import fetch_all


def register_search_jobs_by_title(mcp: FastMCP):
    """Register search_jobs_by_title tool with the MCP server"""

    @mcp.tool()
    def search_jobs_by_title(title: str) -> List[Dict[str, Any]]:
        """
        Searches for jobs by partial or full title and returns matching jobs.

        Args:
            title: Full or partial job title to search for

        Returns:
            A list of dictionaries containing job id and title
        """
        search_query = "SELECT id, title FROM jobs WHERE title ILIKE %s ORDER BY title"
        try:
            # Use % wildcards for partial title matching
            search_param = f"%{title}%"
            results = fetch_all(search_query, (search_param,))

            # Convert the results to a list of dictionaries
            jobs = []
            for row in results:
                jobs.append({"id": row[0], "title": row[1]})

            print(f"Found {len(jobs)} jobs matching '{title}'")
            return jobs
        except Exception as e:
            print(f"An error occurred while searching jobs by title: {e}")
            return []
