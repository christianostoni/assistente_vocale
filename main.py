from jarvis import assistente
import json
from time import sleep

api_key = "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"

assistente_istance = assistente(api_key)

while True: 
        assistente_istance.text = ""
        assistente_istance.riconoscimento()
        if(assistente_istance.text != ""):
                print("testo riconosciuto......")
                assistente_istance.chatGpt()
                assistente_istance.text_to_speech()                



