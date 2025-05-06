from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

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


def generate_response(prompt):

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hi there!"},
        {"role": "assistant", "content": "Hello! How can I assist you today?"},
        {"role": "user", "content": prompt},
    ]
    template = tokenizer.apply_chat_template(messages, tokenize=False)
    input_ids = tokenizer.encode(template, return_tensors="pt").to(model.device)
    outputs = model.generate(
        input_ids,  # input_ids is the input tensor
        max_new_tokens=1000,  # max_new_tokens is the maximum number of tokens to generate
        temperature=0.9,  # temperature controls the randomness of predictions
        top_p=0.95,  # top_p is the cumulative probability for nucleus sampling
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id,  # pad_token_id is the token used for padding
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


prompt = "What is the capital of France?"

print(generate_response(prompt))
