import requests
import logging


# Configuração básica do logging
logging.basicConfig(
    filename='../Logs/repositoryLogs.log',# Diretório com o arquivo onde os logs serão salvos
    level=logging.ERROR,              # Define o nível de logging
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato da mensagem
)

def recordingCall(token,idCall):
        
        endpointRecord = f"https://app.3c.fluxoti.com/api/v1/calls/{idCall}/recording?api_token={token}"

        response = requests.get(endpointRecord)

        if response.status_code == 200:
            
            recordFile = response.content   

            return {"status":True,"file":recordFile}
    
        else:
            logging.error(f"Método:recordingCall | ID Call:{idCall} | Mensagem: Erro ao consultar o arquivo de gravação.",response.status_code,response.text)

            return {"status":False,"file":None}
