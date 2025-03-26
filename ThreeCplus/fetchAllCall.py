import requests

def fetchAllCalls(baseUrl, params):

    recordsCallsId = []
    current_page = 1

    while True:

        # Atualiza o parâmetro da página na URL
        params['page'] = current_page
        response = requests.get(baseUrl, params=params)
        
        if response.status_code != 200:
            print(f"Erro ao fazer a requisição: {response.status_code} | {response.text}")
            break
        
        data = response.json()
        
        # Extraindo apenas os IDs das chamadas
        calls = data.get('data', [])
        callsIds = [call['id'] for call in calls if 'id' in call]
        recordsCallsId.extend(callsIds)
        
        # Verifica se há próxima página
        pagination = data.get('meta', {}).get('pagination', {})
        totalPages = pagination.get('total_pages', 0)
        
        if current_page >= totalPages:
            break
        
        current_page += 1

    return recordsCallsId




