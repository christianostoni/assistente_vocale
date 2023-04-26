from jarvis import assistente
import json
from time import sleep

with open("secrets.json") as file: 
        secrets = json.load(file)
        api_key = secrets["api_key"]

assistente_istance = assistente(api_key)

while True: 
        assistente_istance.text = ""
        assistente_istance.riconoscimento()
        if(assistente_istance.text != ""):
                print("testo riconosciuto......")
                assistente_istance.chatGpt()
                assistente_istance.text_to_speech()                



