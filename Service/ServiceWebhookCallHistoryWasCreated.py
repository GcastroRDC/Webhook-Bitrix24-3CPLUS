from flask import Flask, request, jsonify
from dotenv import load_dotenv
import logging
from ThreeCplus.recordingCall import recordingCall
from ThreeCplus.processDataCallHistoryWasCreated import processDataCallHistoryWasCreated
from ThreeCplus.getMailingData import getMailingData
from Bitrix.crmTimelineCommentAdd import crmTimelineCommentFileRecord,crmTimelineCommentDataMailing
from Bitrix.businessEvents import bussinesEvents
from sqlite.getConnectionDatabase import getConnectionDatabase
from sqlite.closeConection import closeConection
from sqlite.select import select
from sqlite.delete import delete

# Configuração básica do logging
logging.basicConfig(
    filename='../Logs/repositoryLogs.log',# Diretório com o arquivo onde os logs serão salvos
    level=logging.ERROR,              # Define o nível de logging
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato da mensagem
)

def handleError(message, statusCode):

    return jsonify({"error": message}), statusCode

def ServiceWebhookCallHistoryWasCreated(dataRequest,tokenBitrix,token3cPlus):
    
    try:
         
            dataCallHistWasCreated = processDataCallHistoryWasCreated(dataRequest)

            if int(dataCallHistWasCreated['idStatusCall']) != 7:
            
                return handleError(
                    
                        "Chamada não qualificada para integração",
                        400
                    )
            
            positiveQualifications = {75073,36797,None}

            
            conn,cursor = getConnectionDatabase()

            dataSelect = select(
                 cursor,
                 dataCallHistWasCreated['telephonyId']
                 )
           
            if not dataSelect['status']:
                    
                    return handleError("Nenhum valor retornado na consulta ao banco de dados", 400)
            
            dataQualification = bussinesEvents(
                 tokenBitrix,
                 dataSelect['idDeal'],
                 int(dataCallHistWasCreated['qualificationId'])
                 )

            if dataQualification['status'] and dataQualification['id'] in positiveQualifications:
              
                dataRecord = recordingCall(
                     token3cPlus,
                     dataCallHistWasCreated['IdCall']
                     )
        
                if not dataRecord['status']:
               
                    return handleError("Erro na consulta do arquivo de gravação.", 400)
            
                dataMailing = getMailingData(
                     token3cPlus,
                     dataCallHistWasCreated['IdCall']
                     )
                if not dataMailing['status']:
                   
                    return handleError("Erro ao consultar dados do Mailing.", 400)
                
                statusTimelineFileRecord = crmTimelineCommentFileRecord(
                     tokenBitrix,
                     dataSelect['idDeal'],
                     dataRecord['file']
                     )
                if not statusTimelineFileRecord:
                
                    return handleError("Erro ao adicionar arquivo da gravação na timeline do negócio no CRM Bitrix.", 400)
          
                statusTimelineDataMailing = crmTimelineCommentDataMailing(
                     tokenBitrix,
                     dataSelect['idDeal'],
                     dataMailing['mailing']
                     )
                if not statusTimelineDataMailing:
                
                    return handleError("Erro ao adicionaros dados da chamada na timeline do negócio no CRM Bitrix.", 400)
              
                statusDelete = delete(
                     conn,
                     cursor,
                     dataCallHistWasCreated['telephonyId']
                     )
                if not statusDelete:
                
                    return handleError("Erro ao excluir valor do banco de dados", 400)
              
                closeConection(conn)
            
                return jsonify({"success": f"Sucesso na Integração de Saída (v1)"}), 200
            
          
            statusDelete = delete(
                 conn,
                 cursor,
                 dataCallHistWasCreated['telephonyId']
                 )
            if not statusDelete:
                   
                    return handleError("Erro ao excluir valor do banco de dados", 400)
            
            closeConection(conn)

            return jsonify({"success": f"Sucesso na Integração de Saída (v2)"})
        
    except Exception as e:

        logging.error(f"Erro ao processar a história da chamada: {str(e)}")
        return handleError("Erro interno do servidor", 500)
