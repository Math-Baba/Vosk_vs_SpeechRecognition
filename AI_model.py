import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def ai_response(user_text):
    start = time.time() 
    """Envoie le texte à OpenRouter et écrit la réponse dans output.txt"""
    if not user_text:
        return
    
    conversation_history = [
        {"role": "system", "content": (
            "Tu es un éducateur expert en biodiversité marine qui parle à des enfants de 8 à 14 ans. "
            "Tu expliques avec des mots simples et toujours de façon pédagogique. "
            "Tu ne réponds que sur la vie marine."
        )},
        {"role": "user", "content": user_text}
    ]
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "x-ai/grok-4-fast:free",
        "messages": conversation_history
    }
    
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload
    )
    
    if response.status_code == 200:
        reply = response.json()['choices'][0]['message']['content']
    else:
        reply = f"Erreur {response.status_code} : {response.text}"
    
    # Écriture dans output.txt
    with open("output.txt", "a", encoding="utf-8") as f:
        f.write(reply + "\n")
    
    print("IA :", reply)
    end = time.time()  
    print(f"Temps d'exécution : {end - start:.2f} secondes")