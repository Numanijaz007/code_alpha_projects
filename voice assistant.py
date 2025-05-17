import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import sys

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """ Speaks the given text """
    engine.say(text)
    engine.runAndWait()

def listen():
    """ Listens for voice input and returns text """
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you repeat?")
            return listen()
        except sr.RequestError:
            speak("Speech service is unavailable.")
            return None

def greet_user():
    """ Greets the user based on the time of day """
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I assist you today?")

def handle_command(command):
    """ Processes the given command """
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "what time is it" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")
    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad.exe")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        sys.exit()
    else:
        speak("I'm not sure how to do that yet.")

if __name__ == "__main__":
    greet_user()
    while True:
        command = listen()
        if command:
            handle_command(command)
    
