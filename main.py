from jarvis import assistente
from time import sleep

api_key = "you-api-key"
assistente_istance = assistente(api_key)

while True: 
        assistente_istance.text = ""
        assistente_istance.riconoscimento()
        if(assistente_istance.text != ""):
                print("testo riconosciuto......")
                assistente_istance.chatGpt()
                assistente_istance.text_to_speech()                



