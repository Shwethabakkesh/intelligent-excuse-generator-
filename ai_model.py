import httpx

API_KEY = "your-API-keys-here"  # Your real OpenRouter key
BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "HTTP-Referer": "http://localhost:8501",  # Required by OpenRouter
    "X-Title": "Excuse Generator"
}

def generate_excuse(context, urgency, tone):
    prompt = f"Create a believable excuse for {context} with urgency level {urgency} in a {tone} tone."
    payload = {
        "model": "mistralai/mistral-7b-instruct",  # ✅ FREE model
        "messages": [{"role": "user", "content": prompt}],
    }

    response = httpx.post(BASE_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()

def generate_apology(context):
    prompt = f"Write a sincere apology message for missing {context}."
    payload = {
        "model": "mistralai/mistral-7b-instruct",  # ✅ FREE model
        "messages": [{"role": "user", "content": prompt}],
    }

    response = httpx.post(BASE_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()
