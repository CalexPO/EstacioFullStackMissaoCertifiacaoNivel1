import PySimpleGUI as sg
import settings
from menu import menu

# Carrega theme do sistema
sg.theme('DefaultNoMoreNagging')
sg.set_options(font=('Arial Bold', 16))

Usuario = settings.USUARIO
Senha = settings.SENHA
raiz = settings.raiz

# Criar tela de login
layout = [
    [sg.Text('')],
    [sg.Text('Usuário: ', size=8), sg.InputText(key='usuario')],
    [sg.Text('Senha: ', size=8), sg.InputText(key='senha', password_char='*')],
    [sg.Text('')],
    [sg.Button('Entrar')],
]

Window = sg.Window('Login', layout, finalize=True, size=(400,200), resizable=False)
Window['senha'].bind("<Return>", "_Enter")

while True:
    from telas import Cadastros, Consultas
    event,values=Window.read()  
    
    if event == "senha" + "_Enter":
        print(event)
    
    if event == sg.WIN_CLOSED or event == "SairMenu":
        break
    
    if values['usuario'] == Usuario and values['senha'] == Senha:
        Window.close()
        menu()
        break
    else:
        sg.popup("Usuário ou senha inválidos")
        Window['usuario'].update('')
        Window['senha'].update('')
        Window['usuario'].set_focus()



