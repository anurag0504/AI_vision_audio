import speech_recognition as sr
import pyttsx3
import openai
import webbrowser
import subprocess
import random
import os

class VoiceProcessor:
    def __init__(self, api_key):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        openai.api_key = api_key

    def listen_and_interpret(self):
        """ Listen to microphone and convert speech to text """
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio)
                print("You said:", text)
                return text
            except sr.UnknownValueError:
                self.speak("I did not understand that.")
                return None
            except sr.RequestError as e:
                self.speak("Failed to request results.")
                return None

   

    def generate_response(self, text):
        """ Generate a response using OpenAI's Chat model """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": text}]
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return "Failed to generate response due to: " + str(e)

    def speak(self, text):
        """ Use the text-to-speech engine to verbalize the text """
        print("AI:", text)
        self.engine.say(text)
        self.engine.runAndWait()

    def run(self):
        """ Run the continuous interaction loop """
        while True:
            input_text = self.listen_and_interpret()
            if input_text:
                if "exit" in input_text.lower():
                    self.speak("Goodbye!")
                    break
                elif input_text.startswith('command'):
                    response = self.execute_command(input_text)
                else:
                    response = self.generate_response(input_text)
                self.speak(response)
