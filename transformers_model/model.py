from transformers import AutoModelForCausalLM, AutoTokenizer


class ModelProcessor:
    @staticmethod
    def generate_response(user_message):
        tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
        model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
        inputs = tokenizer.encode(
            user_message + tokenizer.eos_token, return_tensors="pt"
        )
        response = model.generate(
            inputs, max_length=1000, pad_token_id=tokenizer.eos_token_id
        )
        return tokenizer.decode(response[0], skip_special_tokens=True)
