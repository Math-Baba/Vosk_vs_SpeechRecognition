import os
import requests
import speech_recognition as sr
from dotenv import load_dotenv

# Charge la clé API depuis le fichier .env
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Initialisation du recognizer
recognizer = sr.Recognizer()

def record_to_file():
    """Enregistre la voix dans input.txt"""
    try:
        with sr.Microphone() as source:
            print("Parle maintenant...")
            recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio, language="fr-FR")
            
            # Écriture dans input.txt
            with open("input.txt", "a", encoding="utf-8") as f:
                f.write(text + "\n")
            
            return text
    except sr.WaitTimeoutError:
        print("Aucune parole détectée.")
    except sr.UnknownValueError:
        print("Impossible de comprendre.")
    except sr.RequestError as e:
        print(f"Erreur API Google : {e}")
    return None

def ai_response(user_text):
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
        "model": "deepseek/deepseek-chat-v3-0324:free",
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

# Boucle principale
while True:
    user_text = record_to_file()
    ai_response(user_text)
