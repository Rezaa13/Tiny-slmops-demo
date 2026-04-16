import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

def summarize_text(text: str, model: str = "gemma3") -> str:
    prompt = f"""
You are a helpful assistant.
Summarize the following text in exactly 3 short bullet points.
Use simple English.

TEXT:
{text}
""".strip()

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=120)
    response.raise_for_status()

    data = response.json()
    return data["response"].strip()