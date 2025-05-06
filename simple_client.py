import json
from simple_client.llm_utils import LLMUtils
from simple_client.mcp_session import MCPClient
from mcp import ClientSession
from mcp.client.sse import sse_client


async def run_async():
    client = MCPClient()
    await client.setup_streams_and_session()


async def run_agent():
    async with sse_client("http://localhost:8000/sse") as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()
            print("Session initialized")
            prompts = await session.list_prompts()
            tools = await session.list_tools()
            resources = await session.list_resources()
            for prompt in prompts.prompts:
                print(f"Prompt: {prompt.name} (NOT SUPPORTED)")
            for tool in tools.tools:
                func = {
                    "type": "function",
                    "function": {
                        "name": tool.name,
                        "description": tool.description,
                        "parameters": {
                            "type": "object",
                            "properties": tool.inputSchema.get("properties"),
                            "required": tool.inputSchema.get("required"),
                        },
                    },
                }
                print(f"Tool: {json.dumps(func, indent=2)}")
            for resource in resources.resources:
                print(f"Resource: {resource.name} (NOT SUPPORTED)")
    return


# llm_utils = LLMUtils()
# llm_utils.setup_model_and_tokenizer()

# print(llm_utils.generate_response("whats the capital of France?"))
# print(generate_response("Hey How are you?", use_tools=True))
# print(generate_response("What about Germany?", use_tools=True))

if __name__ == "__main__":
    import asyncio

    asyncio.run(run_agent())
