import requests
import logging
import base64
import json

# Configuração básica do logging
logging.basicConfig(
    filename='../Logs/repositoryLogs.log',   # Diretório com o arquivo onde os logs serão salvos
    level=logging.ERROR,              # Define o nível de logging
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato da mensagem
)


def crmTimelineCommentFileRecord(token,idDeal,fileRecord):
        
       
        endpointCrmTimelineCommentAdd = f"https://dominio.bitrix24.com.br/rest/crm.timeline.comment.add?auth={token}"
        
        #Codifique o conteúdo do audio em base64
        encodedFile = base64.b64encode(fileRecord).decode('utf-8')

        bodyDataRecord = {
            
            "fields":
                {
                
                    "ENTITY_ID":idDeal,
                    "ENTITY_TYPE": "deal",
                    "COMMENT": "Arquivo da Gravação na Plataforma 3CPLUS",
                    "FILES":{
                  
                      "fileData":
                      [
                          f"Audio da Gravação - Negócio {idDeal}.mp3",
                          encodedFile
                      ]
                  
              }


            }
        }

        
        # Enviar a solicitação POST
        response = requests.post(endpointCrmTimelineCommentAdd,data=json.dumps(bodyDataRecord),headers={'Content-Type':'application/json'})       

        if response.status_code == 200:
              
                return True
       
        logging.error(f"Método:crmTimelineCommentFileRecord | Nº do Négocio:{idDeal} | Mensagem: Erro ao adicionar o arquivo de gravação na timeline do negócio",response.status_code,response.text)
      
        return False
        

def crmTimelineCommentDataMailing(token,idDeal,dataMailing):
        
        endpointCrmTimelineCommentAdd = f"https://tradscorretora.bitrix24.com.br/rest/crm.timeline.comment.add?auth={token}"
          
        if dataMailing is not None:

                formattedDataMailing = []

                for key, value in dataMailing.items():

                    formattedDataMailing.append(f"{key}: {value}")

                # Junta os resultados em uma única string
                resultDataMailing = "\n".join(formattedDataMailing)
                
                bodyDataMailing = {
                
                "fields":
                    {
                    
                        "ENTITY_ID":idDeal,
                        "ENTITY_TYPE": "deal",
                        f"COMMENT": "Segue abaixo os dados da chamada na plataforma 3C PLUS:\n"+ resultDataMailing,
                    
                }
            }
                responseMailing = requests.post(endpointCrmTimelineCommentAdd,data=json.dumps(bodyDataMailing),headers={'Content-Type':'application/json'})  

                if responseMailing.status_code == 200:
                 
                    return True
                
                else:
                   
                    logging.error(f"Método:crmTimelineCommentDataMailing | Nº do Négocio:{idDeal} | Mensagem: Erro ao criar o comentário na timeline do negócio",responseMailing.status_code,responseMailing.text)
                    return False

        return True
       
      

