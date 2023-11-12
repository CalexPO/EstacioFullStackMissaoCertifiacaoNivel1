import sqlite3
import os, sys

# Localiza raiz do projeto
raiz = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(raiz))

    
# inserindo dados na tabela
def insereDados(tabela, campo1, campo2, campo3, campo4, campo5):

    # Conexão com o banco
    from banco import conexao
    conn = conexao.conexao()

    # definindo um cursor
    cursor = conn.cursor()
        
    try:
        if tabela == "Sistema":
            cursor.execute("""
            INSERT INTO Sistema (nome)
            VALUES ('{}')
            """.format(campo1))
            codigo = cursor.lastrowid
            msn = "Dados inseridos com sucesso. Código: {}".format(codigo)
            
        elif tabela == "Usuario":
            cursor.execute("""
            INSERT INTO Usuario (CPF, Nome)
            VALUES ('{}', '{}')
            """.format(campo1, campo2))
            codigo = cursor.lastrowid
            msn = "Dados inseridos com sucesso. Código: {}".format(codigo)
            
        elif tabela == "PerfilAcesso": 
            cursor.execute("""
            INSERT INTO PerfilAcesso (CodigoSistema, nome, descricao)
            VALUES ('{}', '{}', '{}')
            """.format(campo1, campo2, campo3))
            codigo = cursor.lastrowid
            msn = "Dados inseridos com sucesso. Código: {}".format(codigo)
            
        elif tabela == "PerfilUsuario":
            cursor.execute("""
            INSERT INTO PerfilUsuario (CodigoUsuario, CodigoPerfilAcesso)
            VALUES ('{}', '{}')
            """.format(campo1, campo2))
            codigo = cursor.lastrowid
            msn = "Dados inseridos com sucesso. Código: {}".format(codigo)
            
        elif tabela == "MatrizSoD":
            cursor.execute("""
            INSERT INTO MatrizSoD (CodigoPerfilAcesso1, CodigoPerfilAcesso2, Descricao)
            VALUES ('{}', '{}', '{}')
            """.format(campo1, campo2, campo3))
            codigo = cursor.lastrowid
            msn = "Dados inseridos com sucesso. Código: {}".format(codigo)
        
        conn.commit()
        conn.close()
        return msn
        
    except sqlite3.Error as erro:
    
        mensagemErro = str(erro)
        
        if  "UNIQUE" in str(erro):
            msn = "Informação já cadastrada. \nCampos: {}".format(mensagemErro[26:])
            msn = msn.replace("Sistema.", "")
            conn.rollback()
            conn.close()
            return msn       
        
        else:            
            msn = "Erro ao inserir dados. Msg: {}".format(mensagemErro)
            conn.rollback()
            conn.close()    
            return msn