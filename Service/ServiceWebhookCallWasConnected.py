from flask import Flask, request, jsonify
from dotenv import load_dotenv
import logging
from ThreeCplus.recordingCall import recordingCall
from ThreeCplus.processDataWasCreated import processDataWasCreated
from Bitrix.crmContactGet import crmContactGet
from Bitrix.crmDealAdd import crmDealAdd
from Bitrix.businessEvents import bussinesEvents
from Bitrix.userDelegation import userDelegation
from sqlite.getConnectionDatabase import getConnectionDatabase
from sqlite.closeConection import closeConection
from sqlite.insertInto import insertInto

# Configuração básica do logging
logging.basicConfig(
    filename='../Logs/repositoryLogs.log',# Diretório com o arquivo onde os logs serão salvos
    level=logging.ERROR,              # Define o nível de logging
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato da mensagem
)


def handleError(message, statusCode):

    return jsonify({"error": message}), statusCode

def ServiceWebhookCallWasConnected(dataRequest,tokenBitrix):
    
    try:

        dataCallWasConnected = processDataWasCreated(dataRequest)
        
        conn,cursor = getConnectionDatabase()

        dataDelegation = userDelegation(int(dataCallWasConnected['idAgent']))
        if not dataDelegation['status']:
    
            return handleError("Erro na delegação automática do usuário.", 400)
        
        dataContactGet = crmContactGet(
            tokenBitrix,
            int(dataCallWasConnected['identificador'])
            )
        if not dataContactGet['status']:
      
            return handleError("Erro ao consultar dados do contato no Bitrix.", 400)

        dataCrmDealAdd = crmDealAdd(
            tokenBitrix,dataContactGet['contactName'],
            int(dataCallWasConnected['identificador']),
            dataDelegation['idBitrix']
            )
        if not dataCrmDealAdd['status']:
       
            return handleError("Erro ao criar o negócio no Bitrix.", 400)

        statusInsertInto = insertInto(
            conn,
            cursor,
            dataCallWasConnected['telephonyId'],
            int(dataCrmDealAdd['idDeal'])
            )

        if not statusInsertInto:
        
            return handleError("Erro ao inserir valor no banco de dados", 400)
        
        closeConection(conn)
        
        return jsonify({"success": f"Sucesso na Integração de Entrada (v1)"}), 200
    
    except Exception as e:

        logging.error(f"Erro ao processar a conexão: {str(e)}")
        return handleError("Erro interno do servidor", 500)