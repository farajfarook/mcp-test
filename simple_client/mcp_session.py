import json
from mcp import ClientSession
from mcp.client.sse import sse_client


class MCPClient:
    def setup_streams_and_session(self):
        try:
            streams = sse_client("http://localhost:8000/sse")
            self.session = ClientSession(*streams)
            self.session.initialize()
        except Exception as e:
            print(f"Error initializing streams or session to MCP Server: {e}")
            exit()

    def create_message(self, method_name, params, id=None):
        message = {"jsonrpc": "2.0", "method": method_name, "params": params, "id": id}
        return json.dumps(message)

    def send_message(self, message):
        try:
            self.session.send(message.encode())
        except Exception as e:
            print(f"Error sending message to MCP Server: {e}")
