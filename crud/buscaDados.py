import sqlite3
import os, sys

# Localiza raiz do projeto
raiz = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(raiz))


# Consultar informações das tabelas
def buscaDados(tabela, campo, campo1):

    from banco import conexao

    # Conexão com o banco
    conn = conexao.conexao()

    # definindo um cursor
    cursor = conn.cursor()
  
    try:
        if tabela == "Sistema":
            cursor.execute("""
                SELECT 
                    codigo,
                    nome
                     
                FROM Sistema
                WHERE
                    codigo = '{}' or 
                    Nome like('%{}%') or 
                    '{}' = '*'
                                    
                """.format(campo, campo, campo))
            dados = cursor.fetchall()
            return dados

        elif tabela == "Usuario":
            cursor.execute("""
                           
                SELECT 
                    codigo,
                    CPF,
                    Nome
                 
                FROM Usuario
                WHERE
                    codigo = '{}' or 
                    Nome like('%{}%') or 
                    '{}' = '*'

                """.format(campo, campo, campo))
            dados = cursor.fetchall()
            return dados

        elif tabela == "PerfilAcesso":
            cursor.execute("""

                SELECT 
                    codigo,
                    Nome,
                    (select Nome from Sistema where codigo = codigoSistema limit 1) as NomeSistema                 
                FROM PerfilAcesso
                WHERE
                    codigo = '{}' or 
                    Nome like('%{}%') or 
                    '{}' = '*'

                """.format(campo, campo, campo))
            dados = cursor.fetchall()
            return dados

        elif tabela == "PerfilUsuario":
            cursor.execute("""

                SELECT 
                    codigo,
                    codigoPerfilAcesso,
                    CodigoUsuario,
                    (select Nome from Usuario where codigo = CodigoUsuario limit 1) as NomeUsuario,
                    (select Nome from PerfilAcesso where codigo = codigoPerfilAcesso limit 1) as NomePerfilAcesso                 
                                                       
                FROM PerfilUsuario
                WHERE
                    codigoUsuario like('%{}%') or
                    (select Nome from Usuario where codigo = CodigoUsuario limit 1) like('%{}%') or 
                    (select Nome from PerfilAcesso where codigo = codigoPerfilAcesso limit 1) like('%{}%') or
                    codigoPerfilAcesso like('%{}%') or
                    '{}' = '*'

                """.format(campo, campo, campo, campo, campo))
            dados = cursor.fetchall()
            return dados
        
        elif tabela == "MatrizSoD":
            cursor.execute("""

                SELECT 
                    codigoPerfilAcesso1,
                    codigoPerfilAcesso2,
                    Descricao,
                    (select Nome from PerfilAcesso where codigo = codigoPerfilAcesso1 limit 1) as NomePerfilAcesso1,
                    (select Nome from PerfilAcesso where codigo = codigoPerfilAcesso2 limit 1) as NomePerfilAcesso2                
           
                FROM MatrizSoD
                WHERE
                    codigo = '{}' or
                    (select Nome from PerfilAcesso where codigo = codigoPerfilAcesso1 limit 1) like('%{}%') or
                    (select Nome from PerfilAcesso where codigo = codigoPerfilAcesso2 limit 1) like('%{}%') or
                    '{}' = '*'

                """.format(campo, campo, campo, campo))
            dados = cursor.fetchall()
            return dados

        elif tabela == "MatrizSoDMensagem":
            cursor.execute("""

                SELECT 
                    Descricao           
                          
                FROM MatrizSoD
                WHERE
                    codigoPerfilAcesso1 = '{}' and
                    codigoPerfilAcesso2 = '{}'

                """.format(campo, campo1))
            dados = cursor.fetchall()
            return dados
            
    except sqlite3.Error as erro:
        print("Erro ao consultar dados. Msg: ", erro)
