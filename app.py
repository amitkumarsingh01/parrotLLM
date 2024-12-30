import pyttsx3
import speech_recognition as sr
from config import Config
from helpers.llm_helper import chat, stream_parser

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Set speech rate
engine.setProperty('volume', 0.9)  # Set volume

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to user input through the microphone."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source)
            user_input = recognizer.recognize_google(audio)
            return user_input
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you repeat?")
            return None
        except sr.RequestError as e:
            speak("There was an error with the speech recognition service.")
            return None

print(f"Welcome to {Config.PAGE_TITLE}")
speak(f"Welcome to {Config.PAGE_TITLE}")

model = "llama3.2:latest"
messages = []

while True:
    user_prompt = listen()
    if user_prompt:
        print(f"You: {user_prompt}")
        messages.append({"role": "user", "content": user_prompt})
        speak("Generating response...")

        llm_stream = chat(user_prompt, model=model)
        response = "".join(stream_parser(llm_stream))
        print(f"Bot: {response}")
        speak(response)

        messages.append({"role": "assistant", "content": response})
