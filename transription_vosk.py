import vosk
import pyaudio
import time
import json
from AI_model import ai_response

# Charger le modèle Vosk (ici modèle français)
model_path = "vosk-model-fr-0.22"
model = vosk.Model(model_path)

# Création d’un objet de reconnaissance vocale avec une fréquence d’échantillonnage de 16 kHz
rec = vosk.KaldiRecognizer(model, 16000)

# Initialisation de PyAudio pour accéder au micro
p = pyaudio.PyAudio()
try:
    # Ouverture du flux audio avec les paramètres requis
    stream = p.open(format=pyaudio.paInt16, # Format audio (16 bits)
                    channels=1, # Mono
                    rate=16000, # Fréquence d’échantillonnage
                    input=True, # Source = micro
                    frames_per_buffer=8192) # Taille des tampons
except Exception as e:
    print(f"Erreur lors de l'ouverture du micro : {e}")
    p.terminate()
    exit(1)

output_file_path = "recognized_text.txt" # Chemin du fichier où sera enregistré le texte reconnu

# Ouverture du fichier en écriture
with open(output_file_path, "w") as output_file:
    start = time.time()
    print("Listening for speech. Say 'Terminate' to stop.")
    while True:
        try:
            # Lire un bloc d’audio depuis le micro
            data = stream.read(4096, exception_on_overflow=False)

            # Vérifier si une phrase complète a été reconnue
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result()) # Résultat en JSON
                recognized_text = result['text'] # Extraire le texte reconnu

                # Écrire le texte dans le fichier et l’afficher à l’écran
                output_file.write(recognized_text + "\n")
                output_file.flush()
                print(recognized_text)

                ai_response(recognized_text)

                # Vérifier si le mot-clé "terminé" est dit = arrêt du programme
                if "terminé" in recognized_text.lower().split():
                    print("Termination keyword detected. Stopping...")
                    break
        except Exception as e:
            print(f"Erreur pendant la lecture audio ou la reconnaissance : {e}")
            break
    end = time.time()  # fin chrono
    print(f"Temps d'exécution : {end - start:.2f} secondes")

# Fermer proprement le flux et PyAudio
stream.stop_stream()
stream.close()
p.terminate()