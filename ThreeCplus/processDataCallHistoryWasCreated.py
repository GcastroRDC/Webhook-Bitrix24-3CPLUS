

def processDataCallHistoryWasCreated(jsonDataOutboard):

  # Acessa a chave "call-history-was-created" e extrai os valores
    historyData = jsonDataOutboard.get('call-history-was-created', {})

    idCall = historyData.get('_id')
    idStatusCall = historyData.get('status')
    qualificationId = historyData.get('qualification', {}).get('id')
    telephonyId = historyData.get('telephony_id')

    return {
        
        "IdCall":idCall,
        "idStatusCall":idStatusCall,
        "qualificationId":qualificationId,
        "telephonyId":telephonyId

        }

