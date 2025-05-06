from mcp import ClientSession, Tool
from mcp.client.sse import sse_client
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import asyncio


# Initialize the SSE client
def get_parsed_tools(tool: Tool):
    return {
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


# Initialize the list to store parsed tools
parsed_tools = []


async def fetch_parsed_tools():
    async with sse_client("http://localhost:8000/sse") as stream:
        async with ClientSession(*stream) as session:
            await session.initialize()
            print("Session initialized")
            tools = await session.list_tools()
            for tool in tools.tools:
                parsed_tool = get_parsed_tools(tool)
                parsed_tools.append(parsed_tool)
                print(f"Tool: {tool.name}")
    return


asyncio.run(fetch_parsed_tools())


# Initialize the model and tokenizer
models = {
    "llama_3b": "meta-llama/Llama-3.2-3B-Instruct",
    "llama_1b": "meta-llama/Llama-3.2-1B-Instruct",
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


def generate_response(prompt):
    history = [
        {
            "role": "system",
            "content": (
                "You are a helpful assistant. Only use tools when **explicitly asked** to do so. "
                "Do not use tools for general questions; answer directly whenever possible."
            ),
        },
        {"role": "user", "content": "Hi there!"},
        {"role": "assistant", "content": "Hello! How can I assist you today?"},
        {"role": "user", "content": prompt},
    ]
    template = tokenizer.apply_chat_template(
        history, tools=parsed_tools, tokenize=False
    )
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
    return response


if __name__ == "__main__":
    print(generate_response("get all jobs?"))
