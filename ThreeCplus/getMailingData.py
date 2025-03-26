import requests
import logging

# Configuração básica do logging
logging.basicConfig(
    filename='../Logs/repositoryLogs.log',# Diretório com o arquivo onde os logs serão salvos
    level=logging.ERROR, # Define o nível de logging
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato da mensagem
)


def getMailingData(token,idCall):

        endpointCall = f"https://app.3c.fluxoti.com/api/v1/calls/{idCall}?api_token={token}"
        response = requests.get(endpointCall)

        if response.status_code == 200:
           
            dataJson = response.json()

            registersCalls = dataJson.get('data', None)
            mailingData = dataJson.get('data', None).get('mailing_data', None).get('data', None) # Verifica se a chave "data" existe na estrutura do Mailing

            if mailingData is not None:
                 
                mailingData['numero'] = registersCalls['number']
                mailingData['Qualificacao'] = registersCalls['qualification']

              
                return {"status:":True,"mailing":mailingData}
                
            return {"status":True,"mailing":None}
        
        logging.error(f"Método:getMailingData | ID Call:{idCall} | Mensagem: Erro ao consultar os dados do Mailing da chamada",response.status_code,response.text)
        return {"status":False,"mailing":None}
    
