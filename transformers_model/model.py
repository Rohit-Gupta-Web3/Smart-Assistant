import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Huggingface Model Endpoint and Token
model_endpoint = os.getenv("HUGGINGFACE_URL")
api_token = os.getenv("HUGGINGFACE_API_TOKEN")

if not model_endpoint or not api_token:
    raise ValueError("Missing HUGGINGFACE_URL or HUGGINGFACE_API_TOKEN in .env file")

headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json",
}


def generate_response(prompt, max_tokens=512):
    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "model": "mistralai/Mistral-7B-Instruct-v0.3",
        "stream": False,  # 🚀 NORMAL, non-streaming
    }

    response = requests.post(model_endpoint, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"Request failed: {response.status_code}, {response.text}")

    data = response.json()

    try:
        return data["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError) as e:
        raise Exception(f"Unexpected response format: {data}") from e
