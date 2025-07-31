import requests
import json

def get_jarvo_response(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            headers={"Content-Type": "application/json"},
            data=json.dumps({
                "model": "tinyllama",
                "messages": [
                    {"role": "system", "content": "You are Jarvo, a helpful and witty AI assistant."},
                    {"role": "user", "content": prompt}
                ]
            })
        )
        data = response.json()
        return data["message"]["content"]
    except Exception as e:
        return f"Jarvo error: {str(e)}"
