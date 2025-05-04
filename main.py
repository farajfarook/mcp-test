from typing import Any
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


if __name__ == "__main__":
    mcp.run("sse")
