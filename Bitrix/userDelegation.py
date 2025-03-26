import logging

def userDelegation(idRamal):

    ListRamaisxBitrix =[
        
        {"idRamal":53178,"idBitrix":34},
        {"idRamal":57486,"idBitrix":24},
        {"idRamal":101258,"idBitrix":58},
        {"idRamal":72149,"idBitrix":38},
        {"idRamal":62716,"idBitrix":40},
        {"idRamal":101256,"idBitrix":90},
        {"idRamal":101254,"idBitrix":86},
        {"idRamal":101840,"idBitrix":100}, 
        {"idRamal":57934,"idBitrix":12},
        {"idRamal":96731,"idBitrix":28},
        {"idRamal":54544,"idBitrix":14},
        {"idRamal":56223,"idBitrix":16},
        {"idRamal":101257,"idBitrix":88},
        {"idRamal":55144,"idBitrix":74},
        {"idRamal":90919,"idBitrix":22},
        {"idRamal":57932,"idBitrix":10},
        {"idRamal":110109,"idBitrix":26},
        {"idRamal":101255,"idBitrix":92},
        {"idRamal":57486,"idBitrix":24},
        {"idRamal":57933,"idBitrix":8}
    ]
        
    for id in ListRamaisxBitrix:

        if id['idRamal'] == int(idRamal):

            return {"status":True,"idBitrix":id['idBitrix']}
        
    logging.error(f"Método:userDelegation | ID Ramal:{idRamal} | Mensagem: Erro na delegação automática,usuário não identificado.")
    return {"status":False,"idBitrix":None}