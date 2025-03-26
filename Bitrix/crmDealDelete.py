import requests
import logging

# Configuração básica do logging
logging.basicConfig(
    filename='../Logs/repositoryLogs.log',   # Diretório com o arquivo onde os logs serão salvos
    level=logging.ERROR,              # Define o nível de logging
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato da mensagem
)

def crmDealDelete(tokenBitrix,idDeal):

    endpointCrmDealDelete = f"https://dominio.bitrix24.com.br/rest/crm.deal.delete?auth={tokenBitrix}&ID={idDeal}"

    response = requests.post(endpointCrmDealDelete)

    if response.status_code == 200:

        return True
    
    else:
        logging.error(f"Método:crmDealDelete | ID Deal:{idDeal} | Mensagem: Erro ao excluir negócio no CRM Bitrix.",response.status_code,response.text)
        return False
