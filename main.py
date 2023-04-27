from jarvis import assistente
import json
from time import sleep

api_key = "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"
#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
assistente_istance = assistente(api_key)

while True: 
        assistente_istance.text = ""
        assistente_istance.riconoscimento()
        if(assistente_istance.text != ""):
                print("testo riconosciuto......")
                assistente_istance.chatGpt()
                assistente_istance.text_to_speech()                



