import json
from mcp import ClientSession
from mcp.client.sse import sse_client


class MCPClient:
    async def setup_streams_and_session(self):
        try:
            stream = await sse_client("http://localhost:8000/sse")
            session = ClientSession(stream.read, stream.write)
            await session.initialize()
            prompts = await session.list_prompts()
            tools = await session.list_tools()
            resources = await session.list_resources()
            for prompt in prompts.prompts:
                print(f"Prompt: {prompt['name']}")
            for tool in tools.tools:
                func = {
                    "type": "function",
                    "function": {
                        "name": tool["name"],
                        "description": tool["description"],
                        "parameters": {
                            "type": "object",
                            "properties": tool["inputSchema"]["properties"],
                            "required": tool["inputSchema"]["required"],
                        },
                    },
                }
                print(f"Tool: {json.dumps(func, indent=2)}")
            for resource in resources.resources:
                print(f"Resource: {resource['name']}")
        except Exception as e:
            print(f"Error initializing streams or session to MCP Server: {e}")
            exit()
