import requests
import logging

# Configuração básica do logging
logging.basicConfig(
    filename='../Logs/repositoryLogs.log',   # Diretório com o arquivo onde os logs serão salvos
    level=logging.ERROR,              # Define o nível de logging
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato da mensagem
)

def crmDealAdd(token,contactName,idContact,idUserBitrix):

    endpointCrmDealAdd = f"https://dominio.bitrix24.com.br/rest/crm.deal.add?auth={token}"

    headers = {
        
        'Content-Type': 'application/json',
    }

    # Dados do negócio 
    data = {
        f'FIELDS': {
            'TITLE': contactName,
            'TYPE_ID': 'SALE',
            'STAGE_ID': 'C10:NEW', #Etapa do Negócio:CAIXA DE ENTRADA
            'CATEGORY_ID': '10',  #Pipeline PROSPECÇÃO
            'OPPORTUNITY': '0.00',  # Valor do negócio
            'CURRENCY_ID': 'BRL', #Moeda
            'CONTACT_ID':idContact, # ID do Contato
            'ASSIGNED_BY_ID':idUserBitrix  # ID do responsável pelo negócio
        }
    }

    # Enviar a requisição POST
    response = requests.post(endpointCrmDealAdd, json=data, headers=headers)

    # Verificar a resposta
    if response.status_code == 200:

        dataJson = response.json()
        idDeal = dataJson['result']

        return {"status":True,"idDeal":idDeal}
    
    else:
        
        logging.error(f"Método:crmDealAdd | ID Contato:{idContact} | Nome Contato:{contactName} | Mensagem: Erro ao criar o negócio no Bitrix.",response.status_code,response.text)
        return  {"status":False,"idDeal":None}