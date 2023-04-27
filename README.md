Questo è un'assistente vocale, di nome jarvis, realizzato mediante l'utilizzo dell'api di openAi, che ci fornisce un accesso gratuito al modello linguistico di chatGpt. 
Il suo funzionamento è piuttosto semplice: 
1. Con l'utilizzo della libreria SpeechRecognition, viene tradotta in un testo la nostra richiesta audio
2. Il testo viene inviato a chatGpt mediante la sua api. 
3. ChatGpt invia la risposta
4. Mediante la libreria gTTS(google text to speech), la risposta viene convertita in un file audio e salvato sul dispositivo. 
5. Il file audio viene riprodotto utilizzando la libreria playsound. 

Per provare Jarvis, è possibile scaricare la release, nell'apposita sezione di GitHub. 

![immagine](https://user-images.githubusercontent.com/86129489/234898138-d4ea7de1-fa1b-4b56-b7e4-ce2e22ddf2a3.png)

Per visionare, testare e modificare il codice è necessario aver installato l'interprete python e procedere in questo modo: 
1. Spostarsi nella cartella nella quale si vuole copiare il progetto
2. Aprire il terminale nella cartella da utilizzare
3. Clonare la repository con il seguente comando: `git clone https://github.com/christianostoni/assistente_vocale` 
4. Spostarsi con il terminale, nella cartella appena creata nominata assistente_vocale, mediante il seguente comando: `cd assistente_vocale`
5. Eseguire da terminale il seguente comando per scaricare i pacchetti necessari: `pip install -r requirements.txt`
6. Eseguire da terminale il file main.py con il seguente comando: `python main.py', rimanendo sempre nella medesima directory`

