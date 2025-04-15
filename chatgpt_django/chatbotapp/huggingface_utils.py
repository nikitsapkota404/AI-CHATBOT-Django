import os
from dotenv import load_dotenv
import requests

load_dotenv(dotenv_path="api.env") 

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
HF_TOKEN = os.getenv("HF_TOKEN")  # Fetch from .env

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def get_response(message):
    try:
        data = {
            "inputs": f"[INST] {message} [/INST]",
            "parameters": {
                "max_new_tokens": 100,
                "return_full_text": False
            }
        }

        response = requests.post(API_URL, headers=headers, json=data, timeout=10)
        response.raise_for_status()

        full_response = response.json()[0]['generated_text']
        return full_response.replace(f"[INST] {message} [/INST]", "").strip()

    except Exception as e:
        print(f"Error: {str(e)}")
        return "Sorry, I'm having some technical difficulties."

user_input = input("You: ")
reply = get_response(user_input)
print(f"Bot: {reply}")
