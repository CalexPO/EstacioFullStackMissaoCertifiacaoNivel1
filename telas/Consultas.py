import PySimpleGUI as sg
import os, sys

from banco.conexao import database

# Inicia classe banco conexão
db = database()

def telas(tela, filtro):

    sg.theme('DefaultNoMoreNagging')
    # sg.theme('DarkBlue')
    sg.set_options(font=('Arial Bold', 16))

    if tela == "Sistema":
        resultado = db.selectValues(f"{tela}", filtro, "")
        print(resultado)
        layout = [  
            [sg.Text('Pesquisa:', size = (8, 1), font=('Arial', 14)), sg.InputText(enable_events=True, key='-filtro-') ], 
            [sg.Text('')],      
            [sg.Table(
                values=resultado, 
                headings=['CÓDIGO', 'NOME'], 
                col_widths=[7,30],
                justification='left',
                num_rows=10,
                auto_size_columns=False,
                key='-table-',
                enable_events=True
                )
             ],
            [sg.Text('')],      
            [sg.Push(), sg.Button("Sair")]
        ] 

    elif tela == "Usuario":
        resultado = db.selectValues(f"{tela}", filtro, "")
        layout = [  
            [sg.Text('Pesquisa:', size = (8, 1), font=('Arial', 14)), sg.InputText(enable_events=True, key='-filtro-') ], 
            [sg.Text('')],      
            [sg.Table(
                values=resultado, 
                headings=['CÓDIGO', 'CPF', 'NOME'], 
                col_widths=[7, 14, 20],
                justification='left',
                num_rows=10,
                auto_size_columns=False,
                key='-table-'
                )
             ],
            [sg.Text('')],      
            [sg.Push(), sg.Button("Sair")]
        ]

    elif tela == "PerfilAcesso":
        resultado = db.selectValues(f"{tela}", filtro, "")
        lista = []
        for i in resultado:
            lista.append([i[2], i[1]])
        
        resultado=lista
        
        layout = [  
            [sg.Text('Pesquisa:', size = (8, 1), font=('Arial', 14)), sg.InputText(enable_events=True, key='-filtro-') ], 
            [sg.Text('')],      
            [sg.Table(
                values=resultado, 
                headings=['SISTEMA', 'PERFIL ACESSO'], 
                col_widths=[15,25],
                justification='left',
                num_rows=10,
                auto_size_columns=False,
                key='-table-'
                )
             ],
            [sg.Text('')],      
            [sg.Push(), sg.Button("Sair")]
        ]

    elif tela == "PerfilUsuario":
        resultado = db.selectValues(f"{tela}", filtro, "")
        lista = []
        for i in resultado:
            lista.append([i[3], i[4]])
        
        resultado=lista
        
        layout = [  
            [sg.Text('Pesquisa:', size = (8, 1), font=('Arial', 14)), sg.InputText(enable_events=True, key='-filtro-') ], 
            [sg.Text('')],      
            [sg.Table(
                values=resultado, 
                headings=['USUARIO', 'PERFIL ACESSO'], 
                col_widths=[15,25],
                justification='left',
                num_rows=10,
                auto_size_columns=False,
                key='-table-'
                )
             ],
            [sg.Text('')],      
            [sg.Push(), sg.Button("Sair")]
        ]

    elif tela == "MatrizSoD":
        resultado = db.selectValues(f"{tela}", filtro, "")
        lista = []
        for i in resultado:
            lista.append([i[3], i[4]])
        
        resultado=lista
        
        layout = [  
            [sg.Text('Pesquisa:', size = (8, 1), font=('Arial', 14)), sg.InputText(enable_events=True, key='-filtro-') ], 
            [sg.Text('')],      
            [sg.Table(
                values=resultado, 
                headings=['PERFIL ACESSO 1', 'PERFIL ACESSO 2'], 
                col_widths=[20,20],
                justification='left',
                num_rows=10,
                auto_size_columns=False,
                key='-table-'
                )
             ],
            [sg.Text('')],      
            [sg.Push(), sg.Button("Sair")]
        ]
                        
    Window = sg.Window (
        'Consulta: {}'.format(tela),
        layout, size=(550,450),
    )

    while True:
        event,values=Window.read()
        
        print(event, values)
        
        if event == "-filtro-":
            filtro = values["-filtro-"]
            resultado = db.selectValues(f"{tela}", filtro, "")

            # Carrega informações particulares das telas:

            if tela == "PerfilAcesso":
                lista = []
                for i in resultado:
                    lista.append([i[2], i[1]])                    
                resultado=lista

            if tela == "PerfilUsuario":
                lista = []
                for i in resultado:
                    lista.append([i[3], i[4]])
                resultado=lista

            if tela == "MatrizSoD":
                lista = []
                print(resultado)
                for i in resultado:
                    lista.append([i[3], i[4]])
                resultado=lista
                
            # Carrega lista na tabela:
            Window["-table-"].update(resultado)
                                                    
        if event == "Sair":
            Window.close()

        if event == sg.WIN_CLOSED:
            break

    return event,values
