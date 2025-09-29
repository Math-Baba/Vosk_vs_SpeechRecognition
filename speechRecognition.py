import speech_recognition as sr
import time
from AI_model import ai_response

# Initialisation du recognizer
recognizer = sr.Recognizer()

def record_to_file():
    start = time.time()
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

    end = time.time()  # fin chrono
    print(f"Temps d'exécution : {end - start:.2f} secondes")

    return None
    

# Boucle principale
while True:
    user_text = record_to_file()
    print(user_text)
    ai_response(user_text)
