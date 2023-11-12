import PySimpleGUI as sg

class Form:
    def __init__(self, tela, informacoes):
        self.sg = sg
        self.tela = tela
        self.informacoes = informacoes
    
    def telas(self):
            
        self.corpo = self.informacoes
        self.layoutRodape = [
            [sg.Push(), sg.Button("Consulta"), sg.Button("Salvar"), sg.Button("Sair")]
        ]

        self.layout = [
            [sg.Column(self.corpo, justification='left', element_justification='left', vertical_alignment='center')],
            [sg.Text('')],
            [sg.Column(self.layoutRodape , justification='right', element_justification='right', vertical_alignment='down')],
        ]
    
        return self.layout
    
    def janela(self):
        return self.sg.Window(self.tela, self.telas(), size=(500, 258), finalize=True)
