import requests
import logging

# Configuração básica do logging
logging.basicConfig(
    filename='../Logs/repositoryLogs.log',   # Diretório com o arquivo onde os logs serão salvos
    level=logging.ERROR,              # Define o nível de logging
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato da mensagem
)

def crmContactAdd(token,contactName,number,IdUserBitrix):

    endpointCrmContactAdd = f"https://dominio.bitrix24.com.br/rest/crm.contact.add?auth={token}"
        
    headers = {
        'Content-Type': 'application/json',
    }


    data = {

        f'FIELDS': {
            'NAME': contactName,
            'TYPE_ID': 'UC_2JOJQX',
            'SOURCE_ID': 'CALL',
            "EXPORT": "Y",
            "HAS_PHONE": "Y",
            "ASSIGNED_BY_ID": IdUserBitrix,
            "CREATED_BY_ID": IdUserBitrix,
            "UF_CRM_1718280266":"Integração 3CPLUS",
            'PHONE': [{'VALUE': number, 'VALUE_TYPE': 'WORK', "TYPE_ID": "PHONE"}]
        }
    }

    # Enviar a requisição POST
    response = requests.post(endpointCrmContactAdd, json=data, headers=headers)

    # Verificar a resposta
    if response.status_code == 200:

        dataJson = response.json()
        idContact = dataJson['result']

        return True,idContact
    
    else:

        logging.error(f"Método:crmContactAdd | Nome Contato:{contactName} | Número:{number} | Mensagem: Erro ao criar o contato no Bitrix.",response.status_code,response.text)
       
        return False,None