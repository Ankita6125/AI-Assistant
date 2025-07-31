''''
import os
from datetime import datetime
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

# Main function
def ask_gemini(prompt):
    today = datetime.now().strftime("%B %d, %Y")
    current_time = datetime.now().strftime("%I:%M %p")

    system_prompt = (
        "You are Jarvo, an AI assistant. "
        "Respond ONLY with your name if asked your name. "
        "Respond ONLY with the date if asked for today's date. "
        "Respond ONLY with the time if asked for the time. "
        "If the user asks anything else, respond helpfully and concisely."
        f"\nToday's date is {today} and the current time is {current_time}."
    )

    full_prompt = f"{system_prompt}\n\nUser: {prompt}"
    response = model.generate_content(full_prompt)
    return response.text.strip()
'''
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def ask_jarvo(prompt):
    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        return "Error: OPENROUTER_API_KEY is missing in .env"

    today = datetime.now().strftime("%B %d, %Y")
    current_time = datetime.now().strftime("%I:%M %p")

    system_prompt = (
    "You are Jarvo, an AI assistant. "
    "ONLY reply with 'Jarvo' if the user asks for your name. "
    f"ONLY reply with '{today}' if the user asks for today's date. "
    f"ONLY reply with '{current_time}' if the user asks for the current time. "
    "For any other question, answer helpfully, politely, and concisely like a friendly assistant."
)


    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "http://localhost:8000",  # django server
        "X-Title": "Jarvo Voice Assistant",
        "Content-Type": "application/json"
    }
    


    data = {
    "model": "anthropic/claude-3-haiku",  # Or any other working model
    "messages": [
       {"role": "system", "content": [{"type": "text", "text": system_prompt}]},
        {"role": "user", "content": [{"type": "text", "text": prompt}]}
        ]
    
    }


    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    try:
        response_json = response.json()
    except:
        return f"Error: Invalid JSON Response: {response.text}"

    if response.status_code == 200 and "choices" in response_json:
        return response_json["choices"][0]["message"]["content"].strip()
    else:
        return f"Error: {response.status_code} | {response_json}"

