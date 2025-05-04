from typing import Any, Dict, List
from mcp.server.fastmcp import FastMCP
from pgdb import fetch_all


def register_search_candidates_by_name(mcp: FastMCP):
    """Register search_candidates_by_name tool with the MCP server"""

    @mcp.tool()
    def search_candidates_by_name(name: str) -> List[Dict[str, Any]]:
        """
        Searches for candidates by partial or full name and returns matching candidates.

        Args:
            name: Full or partial candidate name to search for

        Returns:
            A list of dictionaries containing candidate id and name
        """
        search_query = (
            "SELECT id, name FROM candidates WHERE name ILIKE %s ORDER BY name"
        )
        try:
            # Use % wildcards for partial name matching
            search_param = f"%{name}%"
            results = fetch_all(search_query, (search_param,))

            # Convert the results to a list of dictionaries
            candidates = []
            for row in results:
                candidates.append({"id": row[0], "name": row[1]})

            print(f"Found {len(candidates)} candidates matching '{name}'")
            return candidates
        except Exception as e:
            print(f"An error occurred while searching candidates by name: {e}")
            return []
