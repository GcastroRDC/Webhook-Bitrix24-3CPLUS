from datetime import datetime, timedelta
from sqlite.updateTokenBitrix import updateTokenBitrix
from credentials.generatorTokenBitrix import generatorAccessToken

def isTokenValid(conn, cursor):
    # Seleciona o token mais recente do banco de dados
    cursor.execute('SELECT token, created_at FROM tokensBitrix ORDER BY created_at DESC LIMIT 1')
    row = cursor.fetchone()

    if row:
        tokenBitrix, created_at = row
        created_at = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S.%f')
        expiration_time = created_at + timedelta(hours=1)
        
        # Verifica se o token está expirado
        if datetime.now() < expiration_time:
            return tokenBitrix
    
    # Gera um novo token se o anterior estiver expirado ou não existir
    newToken = generatorAccessToken()
    updateTokenBitrix(conn, newToken)
    
    return newToken

