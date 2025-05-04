from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hello-world", "0.1.0")


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


if __name__ == "__main__":
    mcp.run()
