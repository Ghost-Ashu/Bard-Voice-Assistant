from flask import Flask, render_template, request, jsonify
from Bard import Chatbot
import pyttsx3
import speech_recognition as sr
import whisper

app = Flask(__name__, static_folder='static', template_folder='templates')

# Paste your Bard Token (check README.md for where to find yours)
token = "<ADD YOUR BARD SESSION TOKEN>"
# Initialize Google Bard API
chatbot = Chatbot(token)
# Initialize speech recognition
r = sr.Recognizer()
# Initialize Whisper model
tiny_model = whisper.load_model('tiny')
base_model = whisper.load_model('base')

# Initialize pyttsx3 for text-to-speech
engine = pyttsx3.init()
# Get the current speech rate
rate = engine.getProperty('rate')
# Decrease speech rate by 50 words per minute (Change as desired)
engine.setProperty('rate', rate - 50)


def prompt_bard(prompt):
    response = chatbot.ask(prompt)
    return response['content']


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen_for_prompt():
    with sr.Microphone() as source:
        try:
            print("Speak your prompt to Bard.\n")
            # Record prompt
            audio = r.listen(source)
            with open("prompt.wav", "wb") as f:
                f.write(audio.get_wav_data())
            # Transcribe prompt using whisper base model
            result = base_model.transcribe('prompt.wav')
            prompt_text = result['text']
            print("Sending to Bard:", prompt_text, '\n')
            # If prompt is empty, return empty response
            if len(prompt_text.strip()) == 0:
                return ""
            return prompt_text
        except Exception as e:
            print("Error transcribing audio: ", e)
            return ""


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask():
    prompt = request.form['prompt']
    response = prompt_bard(prompt)
    return jsonify({'response': response})


@app.route('/speak', methods=['POST'])
def speak_prompt():
    prompt = request.form['prompt']
    speak(prompt)
    return jsonify({'status': 'success'})


@app.route('/listen', methods=['POST'])
def listen_prompt():
    prompt = listen_for_prompt()
    if prompt:
        response = prompt_bard(prompt)
        speak(response)
        return jsonify({'response': response})
    else:
        return jsonify({'response': 'No prompt recorded.'})


if __name__ == '__main__':
    app.run(debug=True)
