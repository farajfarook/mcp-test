import os
import sys
import json
import warnings
import logging
import asyncio
from typing import Optional, List

from mcp import ClientSession
from mcp.client.sse import sse_client

from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env (e.g., GEMINI_API_KEY)

# Suppress specific warnings
warnings.filterwarnings("ignore")


# Custom JSON encoder for objects with 'content' attribute
class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if hasattr(o, "content"):
            return {"type": o.__class__.__name__, "content": o.content}
        return super().default(o)


# Instantiate Google Gemini LLM with deterministic output and retry logic
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_retries=2,
    google_api_key=os.getenv("GEMINI_API_KEY"),
)

server_url = "http://localhost:8000/sse"

# Global holder for the active MCP session (used by tool adapter)
mcp_client = None


# Main async function: connect, load tools, create agent, run chat loop
async def run_agent():
    global mcp_client
    async with sse_client(url=server_url) as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()
            mcp_client = type("MCPClientHolder", (), {"session": session})()
            tools = await load_mcp_tools(session)
            agent = create_react_agent(llm, tools)
            print("MCP Client Started! Type 'quit' to exit.")
            while True:
                query = input("User: ").strip()
                if query.lower() == "quit":
                    break
                # Send user query to agent and print formatted response
                response = await agent.ainvoke({"messages": query})
                for message in response["messages"]:
                    if message.type == "ai":
                        print(f"Assistant: {message.content}")
    return


# Entry point: run the async agent loop
if __name__ == "__main__":
    asyncio.run(run_agent())
