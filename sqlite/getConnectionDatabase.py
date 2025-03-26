from sqlite.conectorDatabase import conectorDatabase

def getConnectionDatabase():

    conn = conectorDatabase()
    cursor = conn.cursor()
    
    return conn, cursor