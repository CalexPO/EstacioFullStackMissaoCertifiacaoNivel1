from banco.conexao import database
from banco.tables import TABLE
from settings import raiz
import os,sys

def recriarbanco():
    print(raiz)
    
    db = database()


    if os.path.exists(raiz + '/banco/banco.db') == True:
        try:
            resp = db.removebanco()    
            db.closeConnection()
            if resp == "OK":
                print("Banco removido com sucesso!")

            # Cria banco e estrutura das tabelas
            for i in TABLE:
                result = db.creatTable(i)
                print(result)
            
            return ("Banco e tabelas recriados com sucesso!")  

        except:
            return ("Problema ao recriar banco!")    

    else:
        try:

            # Cria banco e estrutura das tabelas
            for i in TABLE:
                result = db.creatTable(i)
                print(result)
            
            return ("Banco e tabelas recriados com sucesso!")  

        except:
            return ("Problema ao recriar banco!")    
    
if __name__ == "__main__":
    recriarbanco()