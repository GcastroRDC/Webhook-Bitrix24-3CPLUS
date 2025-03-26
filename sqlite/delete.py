
def delete(conn,cursor,identificador):

    # Excluir dados
    rowsAffected = cursor.execute(f'''
    DELETE FROM TempNegocios WHERE identificador = ?
    ''', (identificador,))

    if rowsAffected == 0:

        return False

    # Salvar as mudanças
    conn.commit()
    
    return True

