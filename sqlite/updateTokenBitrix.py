from datetime import datetime

def updateTokenBitrix(conn,token):

    conn.execute('''
    INSERT INTO tokensBitrix (token, created_at) VALUES (?, ?)
    ON CONFLICT(id) DO UPDATE SET token = excluded.token, created_at = excluded.created_at
    ''', (token, datetime.now()))

    conn.commit()
    conn.close()
  

