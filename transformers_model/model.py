from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os

# Load model + tokenizer once
model_name = os.getenv("HUGGINGFACE_MODEL")
if not model_name:
    raise ValueError("HUGGINGFACE_MODEL not found in .env file")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)


def generate_response(prompt, max_length=1000):
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    output = model.generate(
        **inputs,
        max_length=max_length,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_p=0.92,
        temperature=0.75,
    )
    response = tokenizer.decode(
        output[:, inputs["input_ids"].shape[-1] :][0], skip_special_tokens=True
    )
    return response.strip()
