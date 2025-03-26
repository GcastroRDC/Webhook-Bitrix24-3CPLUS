import requests
import logging

# Configuração básica do logging
logging.basicConfig(
    filename='../Logs/repositoryLogs.log',   # Diretório com o arquivo onde os logs serão salvos
    level=logging.ERROR,              # Define o nível de logging
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato da mensagem
)

def HandleFields(tokenBitrix,idDeal,stageId,categoryId,qualificationId):

      endpointCrmDealUpdate = f"https://dominio.bitrix24.com.br/rest/crm.deal.update?auth={tokenBitrix}&ID={idDeal}"
            
      headers = {
                
                'Content-Type': 'application/json',
            }

            # Dados do negócio 
      dataFields = {
                f'FIELDS': {
             
                    'TYPE_ID': 'SALE',
                    'STAGE_ID': stageId, 
                    'CATEGORY_ID': categoryId, 
                }
            }

             # Enviar a requisição POST
      response = requests.post(endpointCrmDealUpdate, json=dataFields, headers=headers)

            # Verificar a resposta
      if response.status_code == 200:

                return {"status":True,"id":qualificationId}
            
      return {"status":False,"id":qualificationId}

def bussinesEvents(tokenBitrix,idDeal,qualificationId):

    match qualificationId:

        case 114436: # Movimenta o negócio para pipeline "Campanha e-mail"

            dataHandle = HandleFields (tokenBitrix,idDeal,'C28:NEW','28',qualificationId)

            return dataHandle
            
        case 114438: # Movimenta o negócio para pipeline "Campanha Whats"
            
            dataHandle = HandleFields (tokenBitrix,idDeal,'C54:NEW','54',qualificationId)

            return dataHandle
            
          
        case 75073: # enviar a gravação e Dados da chamada 

            return {"status":True,"id":qualificationId}
        
    
        case 36797: # enviar a gravação e Dados da chamada 

            return {"status":True,"id":qualificationId}

        case 37143: # Mover o negócio para a etapa "Sem interesse" na pipeline de Prospecção

            dataHandle = HandleFields (tokenBitrix,idDeal,'C10:UC_FYFD6L','10',qualificationId)

            return dataHandle
           

        case 36798: # Mover o negócio para a etapa "Sem interesse" na pipeline de Prospecção
            
            dataHandle = HandleFields (tokenBitrix,idDeal,'C10:UC_FYFD6L','10',qualificationId)

            return dataHandle
    
        case 36800: # Mover o negócio para a etapa "Telefone Incorreto" na pipeline de Prospecção

            dataHandle = HandleFields (tokenBitrix,idDeal,'C10:UC_A150L8','10',qualificationId)

            return dataHandle
    
        case 36801: # Mover o negócio para a etapa "Agendamento de Retorno" na pipeline de Prospecção
            
            dataHandle = HandleFields (tokenBitrix,idDeal,'C10:PREPAYMENT_INVOIC','10',qualificationId)

            return dataHandle

        case 36796: # Mover o negócio para a etapa "Ligação Muda/Abandonada" na pipeline de Prospecção

            dataHandle = HandleFields (tokenBitrix,idDeal,'C10:UC_CY2KQJ','10',qualificationId)

            return dataHandle
         
        case None:
             
            return {"status":True,"id":None}
           
        case _: # Qualificação não pertencente ao grupo "Padrão Bitrix"
             
            return {"status":True,"id":qualificationId}
