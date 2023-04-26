import speech_recognition as sr
import openai
import json
from gtts import gTTS
from playsound import playsound
import os

class assistente:
    def __init__(self, api_key):
        text=""
        messaggio = ""
        self.text = text
        self.api_key = api_key
        self.messaggio = messaggio

    def riconoscimento(self):
        print("cosa vuoi chiedere a Jarvis?")
        recognizer_istance = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer_istance.adjust_for_ambient_noise(source, duration=1)
            print("calibrato correttamente")
            audio = recognizer_istance.listen(source)
        
        self.text = recognizer_istance.recognize_google(audio, language="it-IT")
        print("testo riconosciuto: " + self.text)  
        print("INVIO A CHATGPT.....")

    def chatGpt(self):
        openai.api_key= self.api_key
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            temperature = 0.7, 
            messages = [
                {"role": "system", "content": "ti chiami jarvis, sei un'assistente vocale e parli italiano, sei stata creata da christian e sei femmina. "},
                {"role": "user", "content": self.text}
                ]
            )
        self.messaggio = response.choices[0].message.content
        self.riconosciuto = True

    def text_to_speech(self):
        cwd = os.getcwd()
        file = "audio.mp3"
        indirizzo = os.path.join(cwd, file)
        os.remove(indirizzo)
        tts = gTTS(text=self.messaggio, lang="it")
        tts.save("audio.mp3")
        playsound("audio.mp3")