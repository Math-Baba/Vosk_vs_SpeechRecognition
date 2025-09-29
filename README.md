# Comparatif entre Vosk et Google Speech Recognition

- **[Vosk](https://alphacephei.com/vosk/)** : une librairie open-source fonctionnant hors ligne.

**Vosk** est particulièrement adapté dans les contextes où l’utilisation hors ligne est primordiale.  
Il permet d’exécuter la reconnaissance vocale directement sur la machine locale, sans dépendance au réseau.  
Son caractère open-source en fait une solution gratuite et flexible, pouvant être intégrée dans des projets embarqués (IoT, robots, systèmes éducatifs).  
L’absence d’envoi de données vers des serveurs externes garantit aussi un meilleur respect de la vie privée.  
En revanche, la précision et la richesse linguistique dépendent fortement du modèle choisi, et restent plus limitées que celles des solutions cloud.


- **[Google Speech Recognition](https://cloud.google.com/speech-to-text/)** : le service cloud de Google pour la transcription vocale.
  
**Google Speech Recognition**, de son côté, repose sur l’infrastructure cloud de Google.  
Il bénéficie de modèles très avancés, offrant une précision élevée et un support multilingue large (plus de 120 langues et variantes).  
Cette approche est pertinente pour des projets nécessitant une transcription fiable, rapide et capable de traiter un grand volume d’audio.  
Cependant, elle implique une dépendance à Internet, un coût lié à l’utilisation de l’API, et une circulation des données vocales via les serveurs Google, ce qui peut soulever des enjeux de confidentialité.  

## Prérequis
* Python 3 ou supérieur
* Microphone fonctionnel
* Clé API [OpenRouteur](https://openrouter.ai/)

## Installation
1. Cloner le dépôt
```bash
git clone https://github.com/Math-Baba/Vosk_vs_SpeechRecognition.git
cd Vosk_vs_SpeechRecognition
```

2. Créer un requirement.txt
```bash
speechrecognition
pyaudio
vosk
requests
python-dotenv
```

3. Installer les dépendances
```bash
pip install -r requirements.txt
```

4. Préparer la clé API OpenRouter

Créez un fichier .env à la racine du projet et insèrez votre clé API OpenRouteur :
```bash
OPENROUTER_API_KEY=
```

5. Télécharger le modèle Vosk français
   
* Téléchargez le modèle depuis : Vosk French Model
* Décompressez-le et placez le dossier à la racine du projet sous le nom vosk-model-fr-0.22

## Utilisation

1. Script speechRecognition.py (Google Speech Recognition)
```bash
python speech_to_file.py
```
* Lorsque vous parlerez au micro, le texte sera enregistré dans input.txt.
* La réponse IA sera affichée et enregistrée dans output.txt.

2. Script transcription_vosk.py (Vosk hors ligne)
```bash
python transcription_vosk.py
```
* Écoute le micro en continu.
* Le texte reconnu est écrit dans recognized_text.txt.
* Le texte est envoyé à l’IA pour générer une réponse.
* Pour arrêter le script, dire le mot "terminé".

# Auteur
**Math-Baba** - [GitHub](https://github.com/Math-Baba)
