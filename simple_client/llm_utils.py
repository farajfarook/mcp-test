from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


class LLMUtils:

    def setup_model_and_tokenizer(self):

        # Initialize the model and tokenizer
        models = {
            "llama_3b": "meta-llama/Llama-3.2-3B-Instruct",
            "llama_1b": "meta-llama/Llama-3.2-1B-Instruct",
        }
        selected_model = "llama_3b"
        model_name = models[selected_model]
        tokenizer_name = models[selected_model]

        print(f"Loading model: {model_name}")

        try:
            self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
            self.model = AutoModelForCausalLM.from_pretrained(
                model_name,
                device_map="auto",
                torch_dtype=torch.float16,
            )
            print(
                f"Model {model_name} loaded successfully. Device: {self.model.device}"
            )
        except Exception as e:
            print(f"Error loading model or tokenizer: {e}")
            exit()

    def generate_response(self, prompt):
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
        template = self.tokenizer.apply_chat_template(
            history, tools=None, tokenize=False
        )
        input_ids = self.tokenizer.encode(template, return_tensors="pt").to(
            self.model.device
        )
        outputs = self.model.generate(
            input_ids,  # input_ids is the input tensor
            max_new_tokens=1000,  # max_new_tokens is the maximum number of tokens to generate
            temperature=0.9,  # temperature controls the randomness of predictions
            top_p=0.95,  # top_p is the cumulative probability for nucleus sampling
            num_return_sequences=1,
            pad_token_id=self.tokenizer.eos_token_id,  # pad_token_id is the token used for padding
        )
        # Only decode the newly generated tokens (exclude the prompt tokens)
        generated_ids = outputs[0][input_ids.shape[-1] :]
        response = self.tokenizer.decode(generated_ids)
        return response
