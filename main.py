from typing import Any, Dict, List
import httpx
from mcp.server.fastmcp import FastMCP

from pgdb import execute_query, fetch_all, get_db_connection

mcp = FastMCP("PageDown ATS", "0.1.0")


@mcp.tool()
def hello_world(name: str) -> str:
    """
    A simple hello world tool that returns a greeting message.
    """
    return f"Hello, {name}!"


@mcp.tool()
def goodbye_world(name: str) -> str:
    """
    A simple goodbye world tool that returns a farewell message.
    """
    return f"Goodbye, {name}!"


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


@mcp.tool()
def search_candidates_by_name(name: str) -> List[Dict[str, Any]]:
    """
    Searches for candidates by partial or full name and returns matching candidates.

    Args:
        name: Full or partial candidate name to search for

    Returns:
        A list of dictionaries containing candidate id and name
    """
    search_query = "SELECT id, name FROM candidates WHERE name ILIKE %s ORDER BY name"
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


if __name__ == "__main__":
    mcp.run("sse")
