def select(cursor, telephoneId):
    # Consultar dados usando placeholders
    cursor.execute('SELECT idNegocio FROM TempNegocios WHERE identificador = ? ORDER BY identificador DESC LIMIT 1', (telephoneId,))
    rows = cursor.fetchall()

    if not rows:
       
        return {"status": False, "idDeal": None}

    for idDeal in rows:
   
        return {"status": True, "idDeal": idDeal[0]}
