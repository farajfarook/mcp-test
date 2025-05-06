from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "meta-llama/Meta-Llama-3.1-8B-Instruct"
tokenizer_name = "meta-llama/Meta-Llama-3.1-8B-Instruct"

print(f"Loading model: {model_name}")

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

try:
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=(torch.float16 if device == "cuda" else torch.float32),
        device_map="auto",
    )
    print("Model and tokenizer loaded successfully.")
except Exception as e:
    print(f"Error loading model or tokenizer: {e}")
    exit()

print("\nSimple Llama Chat Client")
print("Type 'quit' or 'exit' to end the chat.")
print("------------------------------------")

chat_history_ids = None

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        print("Exiting chat.")
        break

    # Encode the new user input, add the eos_token and return a tensor in Pytorch
    new_user_input_ids = tokenizer.encode(
        user_input + tokenizer.eos_token, return_tensors="pt"
    ).to(device)

    # Append the new user input tokens to the chat history
    bot_input_ids = (
        torch.cat([chat_history_ids, new_user_input_ids], dim=-1)
        if chat_history_ids is not None
        else new_user_input_ids
    )

    # Generate a response while limiting the total chat history to avoid overly long inputs
    chat_history_ids = model.generate(
        bot_input_ids,
        max_new_tokens=150,
        pad_token_id=tokenizer.eos_token_id,
        no_repeat_ngram_size=3,
        do_sample=True,
        top_k=50,
        top_p=0.9,
        temperature=0.7,
    )

    # Decode the last bot reply and print it
    response = tokenizer.decode(
        chat_history_ids[:, bot_input_ids.shape[-1] :][0], skip_special_tokens=True
    )
    print(f"Llama: {response}")

    # Optional: Limit the growth of chat_history_ids to save memory
    if chat_history_ids.shape[-1] > 1024:
        chat_history_ids = chat_history_ids[:, -1024:]
