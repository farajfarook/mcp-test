from simple_client.llm_utils import LLMUtils
from simple_client.mcp_session import MCPClient

client = MCPClient()
client.setup_streams_and_session()

llm_utils = LLMUtils()
llm_utils.setup_model_and_tokenizer()

print(llm_utils.generate_response("whats the capital of France?"))
# print(generate_response("Hey How are you?", use_tools=True))
# print(generate_response("What about Germany?", use_tools=True))
