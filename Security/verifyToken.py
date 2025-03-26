from flask import jsonify
import logging
from dotenv import load_dotenv
import os

# Configuração básica do logging
logging.basicConfig(
    filename='../Logs/repositoryLogs.log', # Diretório com o arquivo onde os logs serão salvos
    level=logging.ERROR,              # Define o nível de logging
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato da mensagem
)

load_dotenv()
tokenWebhook = os.environ["tokenWebhook"]

def verifyToken(tokenRequest): # Verificação do Access Token

    TokenInvalidStates = [None,""]

    if tokenRequest in TokenInvalidStates:
          logging.error(f"Método: verifyToken | Mensagem: Token Não Informado")
          return {"status":False,"message":"Token Não Informado","codeErro":401}
    
    elif tokenRequest != tokenWebhook:
        logging.error(f"Método: verifyToken | Mensagem: Token Inválido")
        return {"status":False,"message":"Token Inválido","codeErro":403}
    
    return {"status":True,"message":"Authorized authentication","codeErro":200}
    
