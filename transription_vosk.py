import vosk
import pyaudio
import json

model_path = "vosk-model-fr-0.22"
model = vosk.Model(model_path)
rec = vosk.KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
try:
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=16000,
                    input=True,
                    frames_per_buffer=8192)
except Exception as e:
    print(f"Erreur lors de l'ouverture du micro : {e}")
    p.terminate()
    exit(1)

output_file_path = "recognized_text.txt"

with open(output_file_path, "w") as output_file:
    print("Listening for speech. Say 'Terminate' to stop.")
    while True:
        try:
            data = stream.read(4096, exception_on_overflow=False)
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                recognized_text = result['text']
                output_file.write(recognized_text + "\n")
                output_file.flush()
                print(recognized_text)
                if "terminé" in recognized_text.lower().split():
                    print("Termination keyword detected. Stopping...")
                    break
        except Exception as e:
            print(f"Erreur pendant la lecture audio ou la reconnaissance : {e}")
            break

stream.stop_stream()
stream.close()
p.terminate()