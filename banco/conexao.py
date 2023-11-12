import sqlite3
import os, sys

# Localiza raiz do projeto
raiz = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(raiz))

# Carrega raiz do projeto
raiz = (sys.path[-1])

class database():

    def __init__(self, db = raiz + '/banco/banco.db') -> None:
        self.db = db
        
    def connect(self):
        self.conn = sqlite3.connect(self.db)

    def closeConnection(self):
        try:
            self.conn.close()
        except:
            pass        

    def removebanco(self):
        self.closeConnection()
        try:
            os.remove(self.db)
            return "OK"
        except Exception as e:
            return f"Erro ao remover banco! Falha: {e}"
        
    def creatTable(self, table):
        self.connect()
        try:
            self.conn.execute(table)
            self.conn.commit()
            self.closeConnection()
            
            return "Tabelas criadas com sucesso!"
        
        except Exception as e:
            self.closeConnection()
            return f"Erro ao criar tabelas! Falha: {e}"

    def campos(self, table):

        self.connect()        
        cursor = self.conn.cursor()
        cursor.execute(f"""
            SELECT *                
            FROM {table}                                
            """)
        
        # Pega descrição das colunas
        dados = cursor.description
        lista = []
        for coluna in dados:
            lista.append(coluna[0])
            
        col = (str(lista))
        campos = (col.replace("[","").replace("]","").replace("'","").replace("codigo, ",""))
        
        self.closeConnection()
                
        return campos
            
    def insertValues(self, tabela, valor):

        campos = self.campos(tabela)
        try:
            self.connect()        
            cursor = self.conn.cursor()
            cursor.execute("""INSERT INTO {} ({}) VALUES {}""".format(tabela, campos, str(valor)))
            self.conn.commit()
            codigo = cursor.lastrowid
            msn = "Dados inseridos com sucesso. Código: {}".format(codigo)

            return(msn)

        except sqlite3.Error as erro:
        
            mensagemErro = str(erro)
            
            if  "UNIQUE" in str(erro):
                msn = "Informação já cadastrada. \nCampos: {}".format(mensagemErro[26:])
                msn = msn.replace("Sistema.", "")
                self.conn.rollback()
                self.conn.close()
                return msn       
            
            else:            
                msn = "Erro ao inserir dados. Msg: {}".format(mensagemErro)
                self.conn.rollback()
                self.conn.close()    
                return msn

    def updateValues(self, tabela, codigo, campo_valor):

        try:
            self.connect()        
            cursor = self.conn.cursor()
            cursor.execute("""UPDATE {} SET {} WHERE codigo = {}""".format(tabela, campo_valor, int(codigo)))
            self.conn.commit()
            msn = "Dados atualizados com sucesso!"

            return(msn)

        except Exception as e:
            return f"Erro ao atualizar dados! Falha: {e}"
        
    def deleteValues(self, tabela, codigo):

        try:
            self.connect()        
            cursor = self.conn.cursor()
            cursor.execute("""DELETE FROM {} WHERE codigo = {}""".format(tabela, int(codigo)))
            self.conn.commit()
            msn = "Dados deletados com sucesso!"

            return(msn)

        except Exception as e:
            return f"Erro ao deletar dados! Falha: {e}"
        
    def selectValues(self, tabela, filtro, filtro1):

        try:
            if tabela == "Sistema":
                self.connect()        
                cursor = self.conn.cursor()
                cursor.execute("""
                    SELECT 
                        codigo,
                        nome
                        
                    FROM Sistema
                    WHERE
                        codigo = '{}' or 
                        Nome like('%{}%') or 
                        '{}' = '*'
                                        
                    """.format(filtro, filtro, filtro))
                dados = cursor.fetchall()
                self.closeConnection()
                
                return dados

            elif tabela == "Usuario":
                self.connect()        
                cursor = self.conn.cursor()
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

                    """.format(filtro, filtro, filtro))
                dados = cursor.fetchall()
                self.closeConnection()
                
                return dados

            elif tabela == "PerfilAcesso":
                self.connect()        
                cursor = self.conn.cursor()
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

                    """.format(filtro, filtro, filtro))
                dados = cursor.fetchall()
                self.closeConnection()
                                
                return dados

            elif tabela == "PerfilUsuario":
                self.connect()        
                cursor = self.conn.cursor()
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

                    """.format(filtro, filtro, filtro, filtro, filtro))
                dados = cursor.fetchall()
                self.closeConnection()
                
                return dados
            
            elif tabela == "MatrizSoD":
                self.connect()        
                cursor = self.conn.cursor()                
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

                    """.format(filtro, filtro, filtro, filtro))
                dados = cursor.fetchall()
                self.closeConnection()
                
                return dados

            elif tabela == "MatrizSoDMensagem":
                self.connect()        
                cursor = self.conn.cursor()                
                cursor.execute("""

                    SELECT 
                        Descricao           
                            
                    FROM MatrizSoD
                    WHERE
                        codigoPerfilAcesso1 = '{}' and
                        codigoPerfilAcesso2 = '{}'

                    """.format(filtro, filtro1))
                dados = cursor.fetchall()
                self.connect()        
                cursor = self.conn.cursor()

                return dados
                
        except sqlite3.Error as erro:
            print("Erro ao consultar dados. Msg: ", erro)
