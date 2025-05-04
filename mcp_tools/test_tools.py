from mcp.server.fastmcp import FastMCP


def register_test_tools(mcp: FastMCP):
    """Register basic demo tools with the MCP server"""

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
