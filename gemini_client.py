import os
import json
import warnings
import asyncio

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
            chat_history = []  # Initialize chat history
            while True:
                query = input("User: ").strip()
                if query.lower() == "quit":
                    break

                # Add user query to chat history
                chat_history.append({"role": "user", "content": query})

                # Send chat history to agent and print formatted response
                try:
                    response = await agent.ainvoke({"messages": chat_history})

                    if "messages" not in response:
                        print("Assistant: [No response generated]")
                        # Remove the last user message if no response was generated
                        chat_history.pop()
                        continue

                    ai_response_content = ""
                    for message in response["messages"]:
                        if hasattr(message, "type"):
                            if message.type == "ai":
                                ai_response_content = message.content
                                print(f"Assistant: {ai_response_content}")
                        else:
                            print(f"Unknown message format: {message}")

                    # Add AI response to chat history
                    if ai_response_content:
                        chat_history.append(
                            {"role": "assistant", "content": ai_response_content}
                        )
                    else:
                        # If AI response was empty or not found, remove the last user message
                        chat_history.pop()

                except Exception as e:
                    print(f"Error processing response: {str(e)}")
                    # Remove the last user message if an error occurred
                    if chat_history and chat_history[-1]["role"] == "user":
                        chat_history.pop()
    return


if __name__ == "__main__":
    asyncio.run(run_agent())
