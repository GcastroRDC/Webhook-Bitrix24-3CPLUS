from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from Security.verifyToken import verifyToken
from Security.getToken import getToken
from Service.ServiceWebhookCallWasConnected import ServiceWebhookCallWasConnected
from Service.ServiceWebhookCallWasConnected import ServiceWebhookCallWasConnected
from sqlite.getConnectionDatabase import getConnectionDatabase
from sqlite.isTokenValid import isTokenValid

app = Flask(__name__)

load_dotenv()

conn,cursor = getConnectionDatabase()

tokenBitrix = isTokenValid(conn,cursor)
token3cPlus=os.environ['token3Cplus']

def handleError(message, statusCode):

    return jsonify({"error": message}), statusCode

@app.route('/webhook/3cplus/call.was.connected', methods=['POST'])
def callWasConnected():
    
    tokenRequest = getToken(request)
    dataVerifyToken = verifyToken(tokenRequest)

    if not dataVerifyToken['status']:
         
         return handleError(dataVerifyToken['message'], dataVerifyToken['codeErro'])
    
    result = ServiceWebhookCallWasConnected(
        request.get_json(),
        tokenBitrix
        )
    
    return result

@app.route('/webhook/3cplus/call.history.was.created', methods=['POST'])
def callHistoryWasCreated():

    tokenRequest =  getToken(request)
    dataVerifyToken = verifyToken(tokenRequest)

    if not dataVerifyToken['status']:
         
         return handleError(dataVerifyToken['message'], dataVerifyToken['codeErro'])
    
    result = ServiceWebhookCallWasConnected(
        request.get_json(),
        tokenBitrix,
        token3cPlus
    )

    return result

if __name__ == '__main__':
    # Carregar configuração do certificado
    cert_file = os.getenv('SSL_CERT_FILE', 'certs/server.crt')
    key_file = os.getenv('SSL_KEY_FILE', 'certs/server.key')
  
    app.run(ssl_context=(cert_file, key_file),host='0.0.0.0',port=443)
