
def insertInto(conn,cursor,identificador,idDeal):


    # Inserir dados
    rowsAffected = cursor.execute(f'''
    INSERT INTO TempNegocios (identificador, idNegocio) VALUES (?, ?)
    ''', (identificador, idDeal))

    if rowsAffected == 0:

        return False
    # Salvar as mudanças
    conn.commit()
    
    return True

    
