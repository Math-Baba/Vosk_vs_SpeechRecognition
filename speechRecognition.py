import speech_recognition as sr

r = sr.Recognizer()

def record_text():
    while(1):
        try: 
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)

                audio = r.listen(source, timeout=5)

                MyText = r.recognize_google(audio, language="fr-FR")

                return MyText

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unkown error occured")
    return

def output_text(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return

while(1):
    text = record_text()
    output_text(text)