import requests
from dotenv import load_dotenv
import os

load_dotenv()
info_appLocal = (f'{os.environ["clientId"]}',f'{os.environ["clientSecrety"]}')
client_id,secret_id = info_appLocal
endpoint = 'https://dominio.bitrix24.com.br/oauth/token/?'
pathToken = "credentials/refrashTokenBitrix.txt"

def generatorAccessToken():
            
            with open(f"{pathToken}","r") as arquivo:
                       refresh_token_Base = arquivo.read() 
            
            link = f'{endpoint}client_id={client_id}&grant_type=refresh_token&client_secret={secret_id}&redirect_uri=http%3A%2F%2Ftest.com%2Fbitrix%2Foauth%2Foauth_test.php&refresh_token={refresh_token_Base}' 

            response = requests.get(link)
            data = response.json()

            with open(f"{pathToken}", "w") as arquivo:
                       arquivo.write(data['refresh_token'])

            return data['access_token']

