from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import re

models = {
    "llama_3b": "meta-llama/Llama-3.2-3B-Instruct",
    "llama_1b": "meta-llama/Llama-3.2-1B-Instruct",
}
selected_model = "llama_3b"
model_name = models[selected_model]
tokenizer_name = models[selected_model]

print(f"Loading model: {model_name}")

try:
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        torch_dtype=torch.float16,
    )
    print(f"Model {model_name} loaded successfully. Device: {model.device}")
except Exception as e:
    print(f"Error loading model or tokenizer: {e}")
    exit()


message_history = [
    {
        "role": "system",
        "content": "You are a helpful assistant. Use tools only when explicitly requested by the user or when necessary; otherwise respond directly without invoking any tools.",
    },
    {"role": "user", "content": "Hi there!"},
    {"role": "assistant", "content": "Hello! How can I assist you today?"},
]

available_tools = [
    {
        "type": "function",
        "function": {
            "name": "get_all_cadidates",
            "description": "Returns all candidates.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        },
    },
]


def add_message(role, content):
    """Adds a message to the message history."""
    message_history.append({"role": role, "content": content})


def generate_response(prompt):
    add_message("user", prompt)
    template = tokenizer.apply_chat_template(
        message_history, tools=available_tools, tokenize=False
    )
    input_ids = tokenizer.encode(template, return_tensors="pt").to(model.device)
    outputs = model.generate(
        input_ids,  # input_ids is the input tensor
        max_new_tokens=1000,  # max_new_tokens is the maximum number of tokens to generate
        temperature=0.9,  # temperature controls the randomness of predictions
        top_p=0.95,  # top_p is the cumulative probability for nucleus sampling
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id,  # pad_token_id is the token used for padding
    )
    # Only decode the newly generated tokens (exclude the prompt tokens)
    generated_ids = outputs[0][input_ids.shape[-1] :]
    response = tokenizer.decode(generated_ids)
    return response


print(generate_response("whats the capital of France?"))
# print(generate_response("Hey How are you?", use_tools=True))
# print(generate_response("What about Germany?", use_tools=True))
