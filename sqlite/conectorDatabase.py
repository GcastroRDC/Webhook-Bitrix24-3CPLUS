import sqlite3

def conectorDatabase():

    # Conectar ao banco de dados (ou criar um novo banco de dados se ele não existir)
    conn = sqlite3.connect('tempDatabase.db')

    return conn



