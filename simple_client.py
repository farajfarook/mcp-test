from mcp import ClientSession, Tool
from mcp.client.sse import sse_client
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import asyncio
import json

models = {
    "llama_1b": "meta-llama/Llama-3.2-1B-Instruct",
    "llama_3b": "meta-llama/Llama-3.2-3B-Instruct",
}
selected_model = "llama_3b"
model_name = models[selected_model]
try:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        torch_dtype=torch.float16,
    )
    print(f"Model {model_name} loaded successfully. Device: {model.device}")
except Exception as e:
    print(f"Error loading model or tokenizer: {e}")
    exit()

mcp_server_url = "http://localhost:8000/sse"

history = [
    {
        "role": "system",
        "content": (
            "You are a helpful assistant. Only use tools when **explicitly asked** to do so. "
            "Do not use tools for general questions; answer directly whenever possible."
        ),
    },
    {"role": "user", "content": "Hi there!"},
    {
        "role": "assistant",
        "content": "Hello! How can I assist you today?",
    },
]


def add_history(role, content):
    history.append({"role": role, "content": content})


class GenResponse:
    def __init__(self, response: str, func: dict):
        self.response = response
        self.func = func

    response: str
    func: dict


def parse_tools(tools):
    parsed_tools = []
    for tool in tools.tools:
        parsed_tool = {
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
        parsed_tools.append(parsed_tool)
        print(f"Tool: {tool.name}")
    return parsed_tools


def generate_response(prompt, tools, role="user") -> GenResponse:
    add_history(role, prompt)
    template = tokenizer.apply_chat_template(history, tools=tools, tokenize=False)
    input_ids = tokenizer.encode(template, return_tensors="pt").to(model.device)
    outputs = model.generate(
        input_ids,  # input_ids is the input tensor
        max_new_tokens=1000,  # max_new_tokens is the maximum number of tokens to generate
        temperature=0.9,  # temperature controls the randomness of predictions
        top_p=0.95,  # top_p is the cumulative probability for nucleus sampling
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id,
    )
    # Only decode the newly generated tokens (exclude the prompt tokens)
    generated_ids = outputs[0][input_ids.shape[-1] :]
    response = tokenizer.decode(generated_ids)

    # Strip out special tokens
    response = response.replace("<|start_header_id|>assistant<|end_header_id|>", "")
    response = response.replace("<|eot_id|>", "")
    response = response.replace("<|eom_id|>", "")
    response = response.strip()
    add_history("assistant", response)
    try:
        json_obj = json.loads(response)
        if isinstance(json_obj, dict) and json_obj.get("type") == "function":
            print("Found valid JSON object with type=function:")
            print(json.dumps(json_obj, indent=2))
        return GenResponse(response, func=json_obj)
    except json.JSONDecodeError:
        return GenResponse(response, func=None)


async def run_async():
    async with sse_client(mcp_server_url) as stream:
        async with ClientSession(*stream) as session:
            await session.initialize()
            print("Session initialized")
            tools = parse_tools(await session.list_tools())

            while True:
                user_input = input("User: ")
                if user_input.lower() == "exit":
                    break

                response = generate_response(user_input, tools)
                while response.func is not None:
                    func = response.func
                    func_name = func.get("function") or func.get("name")
                    func_args = func.get("parameters")
                    print(f"Calling tool: {func_name} with args: {func_args}")
                    tool_response = await session.call_tool(func_name, func_args)
                    tool_response_texts = []
                    for text in tool_response.content:
                        if text.type == "text":
                            tool_response_texts.append(text.text)
                    joined_response_text = "\n\n".join(tool_response_texts)
                    # print("Tool response:", joined_response_text)
                    add_history("tool", joined_response_text)
                    response = generate_response(
                        "Whats the answer in your words", tools
                    )

                print("Assistant:", response.response)
    return


if __name__ == "__main__":
    asyncio.run(run_async())
