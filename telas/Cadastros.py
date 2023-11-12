import PySimpleGUI as sg
import os, sys
from banco.conexao import database

# Inicia classe banco conexão
db = database()

def telas(tela):

    sg.theme('DefaultNoMoreNagging')
    # sg.theme('DarkBlue')
    sg.set_options(font=('Arial Bold', 16))

    if tela == "cadSistema":
        layout = [ 
            [sg.Text('Cadastro do Sistema')], 
            [sg.Text('')], 
            [sg.Text('Nome: ', size = (6, 1), font=('Arial', 14)), sg.InputText(key="-NOME-")], 
            [sg.Text('')], 
            [sg.Text('')],         
            [sg.Text('')],      
            [sg.Push(), sg.Button("Consulta"), sg.Button("Salvar"), sg.Button("Sair")]
            
        ] 
            
        Window = sg.Window (
            'Gerenciamento da Matriz SoD',
            layout, size=(500,258),
        )

        while True:
            event,values=Window.read()
            
            if event == "Salvar":
                
                # Carrega campos
                nome = values["-NOME-"]  
                              
                if  nome == "":
                            sg.popup_auto_close("Preencha todos os campos!")
                            Window["-NOME-"].SetFocus()
                else:
                    try:        
                        mensagem = db.insertValues('Sistema', f"('{nome}')")
                        sg.popup(mensagem)
                        Window["-NOME-"].update("")
                        Window["-NOME-"].SetFocus()                        
                    except:
                        sg.popup_auto_close("Erro no cadastro!")
            
            if event == "Consulta":
                from telas import Consultas
                eventos = Consultas.telas("Sistema", "*")

            if event == "Sair":
                Window.close()

            if event == sg.WIN_CLOSED:
                break

        return event,values
            
    elif tela == "cadUsuario":

        layout  = [ 
            [sg.Text('Cadastro do Usuário')], 
            [sg.Text('')], 
            [sg.Text('CPF:', size = (6, 1), font=('Arial', 14)), sg.InputText(key='-CPF-', size=14, justification="left", enable_events=True) ],  
            [sg.Text('Nome:', size = (6, 1), font=('Arial', 14)), sg.InputText(key='-NOME-') ], 
            [sg.Text('')], 
            [sg.Text('')], 
            [sg.Push(), sg.Button("Consulta"), sg.Button("Salvar"), sg.Button("Sair")]
            
        ] 
            
        Window = sg.Window (
            'Gerenciamento da Matriz SoD',
            layout, size=(500,258),
        )

        while True:
            event,values=Window.read()
            
            from funcoes.utilidades import format_cpf, valida_cpf

            if event == "-CPF-":
                cpf = values["-CPF-"]
                cpfFormatado = format_cpf(cpf)
                
                Window["-CPF-"].update(value=cpfFormatado)
            
            if event == "Salvar":

                if values["-CPF-"] == "" or values["-NOME-"] == "":
                    sg.popup_auto_close("Preencha todos os campos!")
                    Window["-CPF-"].SetFocus()
                                        
                elif valida_cpf(values["-CPF-"]) == False:
                    sg.popup_auto_close("CPF Inválido!")
                    Window["-CPF-"].SetFocus()
                    
                elif valida_cpf(values["-CPF-"]) == True:
                    print("CPF Válido")

                    try:                                        
                        # Carrega campos
                        cpf = values["-CPF-"]
                        nome = values["-NOME-"]

                        mensagem = db.insertValues('Usuario', f" ('{nome}', '{cpf}') ")
                        sg.popup(mensagem)
                        Window["-CPF-"].update("")
                        Window["-NOME-"].update("")
                        Window["-CPF-"].SetFocus()
                        
                    except:
                        sg.popup_auto_close("Erro no cadastro!")

            if event == "Consulta":
                from telas import Consultas
                eventos = Consultas.telas("Usuario", "*")
                print(eventos)

            if event == "Sair":
                Window.close()

            if event == sg.WIN_CLOSED:
                break
            
        return event,values

    elif tela == "cadPerfilAcesso":

        # Carregar Tabelas
        dados1 = db.selectValues(f"Sistema", "*", "")
        ListaUsuario = dict(dados1)
        
        layout = [ 
            [sg.Text('Cadastro do Perfil de Acesso')], 
            [sg.Text('')], 
            [sg.Combo(values=list(ListaUsuario.items()), size=(40,1), readonly=True, default_value='Selecione Sistema', key="csis")],   
            [sg.Text('Nome', size = (10, 1), font=('Arial', 14)), sg.InputText(key='-NOME-') ], 
            [sg.Text('Descrição', size = (10, 1), font=('Arial', 14))], 
            [sg.Multiline(size=(40,5), expand_y=True, key='-DESCRICAO-')], 
            [sg.Text('')], 
            [sg.Push(), sg.Button("Consulta"), sg.Button("Salvar"), sg.Button("Sair")]
            
        ] 
            
        Window = sg.Window (
            'Gerenciamento da Matriz SoD',
            layout, size=(500,400),
        )

        while True:
            event,values=Window.read()
                                 
            if event == "Salvar":

                # Carrega campos preenchidos no formulário
                codigoSistema = values["csis"][0]
                nome = values["-NOME-"]
                descricao = values["-DESCRICAO-"]
                
                if values["csis"] == "Selecione Sistema" or nome == "" or descricao == "":
                    sg.popup_auto_close("Preencha todos os campos!")
                    Window["-NOME-"].SetFocus()
                
                else:
                    try:      
                        mensagem = db.insertValues('PerfilAcesso', f" ('{codigoSistema}', '{nome}', '{descricao}') ")
                        sg.popup(mensagem)
                        Window["-NOME-"].update("")
                        Window["-DESCRICAO-"].update("")
                        Window["-NOME-"].SetFocus()
                    except:
                        sg.popup_auto_close("Erro no cadastro!")

            if event == "Consulta":
                from telas import Consultas
                eventos = Consultas.telas("PerfilAcesso", "*")

            if event == "Sair":
                Window.close()

            if event == sg.WIN_CLOSED:
                break

        return event,values

    elif tela == "cadPerfilUsuario":

        # Carregar dados das Tabelas
        dados1 = db.selectValues(f"Usuario", "*", "")    
        lista = []
        for i in dados1:
            lista.append([i[0], i[2]])
        ListaUsuario=dict(lista)
        
        dados2 = db.selectValues(f"PerfilAcesso", "*", "")  
        lista = []
        for i in dados2:
            lista.append([i[0], i[1]])
        ListaPerfilAcesso=dict(lista)
        
        layout = [ 
            [sg.Text('Cadastro do Perfil do Usuário')], 
            [sg.Text('')], 
            [sg.Combo(values=list(ListaUsuario.items()), size=(40,1), readonly=True, default_value='Selecione Usuário', key="cusu")],   
            [sg.Text('')], 
            [sg.Combo(values=list(ListaPerfilAcesso.items()), size=(40,1), readonly=True, default_value='Selecione Perfil Acesso', key="pfa")],                       
            [sg.Text('')],                     
            [sg.Push(), sg.Button("Consulta"), sg.Button("Salvar"), sg.Button("Sair")]
            
        ] 
            
        Window = sg.Window (
            'Gerenciamento da Matriz SoD',
            layout, size=(500,280),
        )

        while True:
            event,values=Window.read()
                                    
            if event == "Salvar":

                # Carrega campos
                codigoUsuario = values["cusu"][0]
                codigoPerfil = values["pfa"][0]
                                
                # Verifica MatrizSoD
                from funcoes.utilidades import validaMatriz
                resultado = validaMatriz(codigoUsuario, codigoPerfil)
                
                if values["cusu"] == "Selecione Usuário" or values["pfa"] == "Selecione Perfil Acesso":
                    sg.popup_auto_close("Preencha todos os campos!")
                    Window["cusu"].SetFocus()

                else:                                            
                    try:                        
                        if resultado[0] == 'conflito':
                            mens = resultado[1]
                            sg.popup_error("Alerta de Conflito de perfil!!", str(mens[0]).replace('[','')).replace(']','').replace('(','').replace(')','')
                
                        else:
                            mensagem = db.insertValues('PerfilUsuario', f" ('{codigoUsuario}', '{codigoPerfil}') ")
                            Window["cusu"].update('Selecione Usuário')
                            Window["pfa"].update('Selecione Perfil Acesso')
                            sg.popup(mensagem)
                    except:
                        sg.popup_auto_close("Erro no cadastro!")

            if event == "Consulta":
                from telas import Consultas
                eventos = Consultas.telas("PerfilUsuario", "*")

            if event == "Sair":
                Window.close()

            if event == sg.WIN_CLOSED:
                break

        return event,values

    elif tela == "MatrizSoD":

        # Carregar Tabelas        
        dados2 = db.selectValues(f"PerfilAcesso", "*", "")   
        lista = []
        for i in dados2:
            lista.append([i[0], i[1]])
        ListaPerfilAcesso1=dict(lista)

        dados2 = db.selectValues(f"PerfilAcesso", "*", "")   
        lista = []
        for i in dados2:
            lista.append([i[0], i[1]])
        ListaPerfilAcesso2=dict(lista)
        
        layout = [ 
            [sg.Text('Cadastro da Matriz de Conflito')], 
            [sg.Text('')], 
            [sg.Combo(values=list(ListaPerfilAcesso1.items()), size=(40,1), readonly=True, default_value='Selecione Perfil 1 Acesso', key="pfa1", enable_events=True)],                       
            [sg.Combo(values=list(ListaPerfilAcesso2.items()), size=(40,1), readonly=True, default_value='Selecione Perfil 2 Acesso', key="pfa2", enable_events=True)],                       
            [sg.Text('Descrição', size = (10, 1), font=('Arial', 14))], 
            [sg.Multiline(size=(40,5), expand_y=True, key='-DESCRICAO-')], 
            [sg.Text('')], 
            [sg.Push(), sg.Button("Consulta"), sg.Button("Salvar"), sg.Button("Sair")]
            
        ] 
            
        Window = sg.Window (
            'Gerenciamento da Matriz SoD',
            layout, size=(500,400),
        )

        while True:
            event,values=Window.read()
            
            # if event == "pfa1":
                
            #     novaLista = []
            #     perfilSelecao = list(values["pfa1"])
            #     novaLista = lista.remove(perfilSelecao)
            #     # values["pfa2"] = novaLista
            #     Window["pfa2"].update(values=novaLista)

            if event == "Salvar":

                # Carrega campos preechidos no formulario
                codigoPerfil1 = values["pfa1"][0]
                codigoPerfil2 = values["pfa2"][0]
                descricao = values["-DESCRICAO-"]

                if values["pfa1"] == values["pfa2"]:
                    sg.popup_auto_close("O mesmo perfil não pode ser selecionado duas vezes!")
                    Window["-DESCRICAO-"].SetFocus()
            
                elif values["pfa1"] == "Selecione Perfil 1 Acesso" or values["pfa2"] == "Selecione Perfil 2 Acesso" or descricao == "":
                    sg.popup_auto_close("Preencha todos os campos!")
                    Window["-DESCRICAO-"].SetFocus()

                else:                                    
                    try:
                        mensagem = db.insertValues('MatrizSoD', f" ('{codigoPerfil1}', '{codigoPerfil2}', '{descricao}') ")
                        sg.popup(mensagem)                     
                        Window["pfa1"].update("Selecione Perfil 1 Acesso")
                        Window["pfa2"].update("Selecione Perfil 2 Acesso")
                        Window["-DESCRICAO-"].update("")
                    except:
                        sg.popup_auto_close("Erro no cadastro!")

            if event == "Consulta":
                from telas import Consultas
                eventos = Consultas.telas("MatrizSoD", "*")

            if event == "Sair":
                Window.close()

            if event == sg.WIN_CLOSED:
                break

        return event, values
    
if __name__ == "__main__":
    pass