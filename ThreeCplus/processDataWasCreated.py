
def processDataWasCreated(dataEntriesOnboard):

 # Acessa a chave "call-was-connected" e extrai "identifier" e "agent"
    callData = dataEntriesOnboard.get('call-was-connected', {})

    identifier = callData.get('identifier')
    idAgent = callData.get('agent')
    telephonyId = callData.get('telephony_id')
    
    return {"identificador":identifier,"idAgent":idAgent,"telephonyId":telephonyId}