import PySimpleGUI as sg
from settings import raiz, SENHA, SENHA_ACESSO, EQUIPE, TRABALHO

def menu():

    # Carrega theme do sistema
    sg.theme('DefaultNoMoreNagging')
    sg.set_options(font=('Arial Bold', 16))
    
    # criar Layout do Menu
    menu = [
            ['Cadastro',
                [
                    '&Sistema', 
                    '&Usuário'
                    ]
                ],
            ['Configuração de Acesso',
                [
                    'Perfil de &Acesso',
                    '&Matriz de Conflito',
                    '&Perfil do Usuário',
                    ]
                ],
            ['Consulta',
                [
                    'Consulta Sistema',
                    'Consulta Usuário',
                    'Consulta Perfil de Acesso',
                    'Consulta Perfil do Usuário',
                    'Consulta Matriz de Conflito'
                ]
            ],
            ['Sobre',
                [
                    'Informações do Trabalho',
                    'Equipe'
                ],            
            ],
           ['Settings',
                [
                    'Recriar Banco',
                ],            
            ],
    ]

    layout = [
            [sg.MenubarCustom(menu, tearoff=False, pad=(2,0), bar_font=('Arial Bold', 12))], 
            [sg.Image(raiz + '/imagens/ESTACIO-1024x481.png', size=(900,540), 
                      right_click_menu=['$Right',
                                        ['Papel parede',['Paper 1', 'Paper 2', 'Paper 3']],
                                        
                                    ],
                      key='-IMAGE-')
            ],  
            [sg.Push(),sg.Text('Usuário: Administrador  ', font=('Arial Bold', 12, ))],
    ]
    
    Window = sg.Window (
        'Sistema de Gerenciamento de Matriz SoD',
        layout, size=(900,600),
        resizable=False, 
        finalize=True,
        element_justification='jusftify',
        element_padding=(0,0),
        margins=(0,0),
         
    )

    while True:
        from telas import Cadastros, Consultas
        event,values=Window.read()  
        
        if event == sg.WIN_CLOSED or event == "SairMenu":
            break

        elif event == "Paper 1":
            Window['-IMAGE-'].update(raiz + '/imagens/menuplanofundo.png', size=(900,550))
        
        elif event == "Paper 2":
            Window['-IMAGE-'].update(raiz + '/imagens/menuplanofundo1.png', size=(900,550))

        elif event == "Paper 3":
            Window['-IMAGE-'].update(raiz + '/imagens/menuplanofundo2.png', size=(900,550))
        
        elif event == "Sistema":
            Cadastros.telas("cadSistema")

        elif event == "Usuário":
            Cadastros.telas("cadUsuario")

        elif event == "Perfil de Acesso":
            Cadastros.telas("cadPerfilAcesso")

        elif event == "Perfil do Usuário":
            senha = sg.popup_get_text("Digite a Senha de acesso.", size=20, password_char='*')
            if senha == str(SENHA_ACESSO):
                Cadastros.telas("cadPerfilUsuario")

        elif event == "Matriz de Conflito":
            senha = sg.popup_get_text("Digite a Senha de acesso.", size=20, password_char='*')

            if senha == str(SENHA_ACESSO):
                Cadastros.telas("MatrizSoD")

        elif event == "Consulta Sistema":
            Consultas.telas("Sistema", "*")

        elif event == "Consulta Usuário":
            Consultas.telas("Usuario", "*")

        elif event == "Consulta Perfil de Acesso":
            Consultas.telas("PerfilAcesso", "*")

        elif event == "Consulta Perfil do Usuário":
            Consultas.telas("PerfilUsuario", "*")

        elif event == "Consulta Matriz de Conflito":
            Consultas.telas("MatrizSoD", "*")
                    
        elif event == "Equipe":
            lista = []
            for i in EQUIPE:
                lista += ([i[0]+ ": "+ i[1]])
            
            lista = "\n".join(lista)            
            sg.popup(lista, title="Equipe") 
                            
        elif event == "Informações do Trabalho":
            lista = []
            for i in TRABALHO:
                lista += ([i[0]+ ": "+ i[1]])
            
            lista = "\n".join(lista)            
            sg.popup(lista, title="Informaçães do Trabalho") 

        elif event == "Recriar Banco":
            from banco.model import recriarbanco
            resp = ""
            resp = recriarbanco()    
            sg.popup_auto_close(resp)                       

# Para executar o menu diretamente, descomentar a linha abaixo                           
if __name__ == "__main__":
        menu()