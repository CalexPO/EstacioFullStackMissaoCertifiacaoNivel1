from conexao import database
from tables import TABLE
import os

db = database()

# Remove banco se existir
if db:

# Insere dados nas tabela
    sistema = (
            ("Compras"),
            ("Vendas"),
            ("Contabilidade"),
            ("Financeiro"),
            ("Fiscal"),
            ("Diretoria")
        )

    for i in sistema:
        res = db.insertValues('Sistema', f"('{i}')")
        print(res)

    usuario =  (
        ("Carlos", "111.111.111-11"),
        ("Daniel", "980.662.220-09"),
        ("Felipe", "949.107.100-94"),
        ("Marcio", "239.016.680-63")
    )

    for i in usuario:
        res = db.insertValues('Usuario', [i][0])
        print(res)

    PerfilAcesso = {
        (1,"Auxiliar de Compras","Responsável pelo cadastro de fornecedores, produtos, serviços e criação de Orçamentos."),
        (1,"Gerente de Compras","O gerente de comprar poderá fazer uma auditoria dos orçamentos lançados, cadastro financeiro do fornecedor e fornecedores frequentes."),
        (1,"Relatório de Compras","O usuário poderá acessar os relatórios de compras."),
        (2,"Vendedor","O usuário poderá acessar as telas de pedidos, clintes e produtos de venda."),
        (2,"Supervisor Vendas","O usuário terá acesso ás informações dos vendedores como desempenho de vendas e comissões."),
        (2,"Relatório de Vendas","O usuário poderá acessar os relatórios de vendas."),
        (3,"Analista Contabilidade","O usuário terá acesso à todas as informações contábeis dos sistemas e poderá fazer auditorias.")

    }

    for i in PerfilAcesso:
        res = db.insertValues('PerfilAcesso', [i][0])
        print(res)

    db.closeConnection()
    
else:
    print("Erro ao criar tabelas!")