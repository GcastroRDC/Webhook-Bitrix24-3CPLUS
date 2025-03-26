import requests
import logging

# Configuração básica do logging
logging.basicConfig(
    filename='../Logs/repositoryLogs.log',   # Diretório com o arquivo onde os logs serão salvos
    level=logging.ERROR,              # Define o nível de logging
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato da mensagem
)

def crmContactGet(token,idContact):

    endpointcrmContactGet = f"https://dominio.bitrix24.com.br/rest/crm.contact.get?auth={token}&ID={idContact}"

    response = requests.get(endpointcrmContactGet)

    if response.status_code == 200:

        dataJson = response.json()

        result = dataJson['result']
        contactName = result['NAME']

        return {"status":True,"contactName":contactName}
    
    else:
        logging.error(f"Método:crmContactGet | ID Contato:{idContact} | Mensagem: Erro ao consultar o contato no Bitrix.",response.status_code,response.text)
        return  {"status":False,"nameContact":None}