import os, sys

EQUIPE = [
        ['202308511361', 'Carlos Alexandre Paulino de Oliveira'],
        ['202309448467', 'Daniel Guerreiro'],
        ['202307014788', 'Matheus Macêdo Sousa']
]

TRABALHO = [
        ['Curso', 'Desenvolvimento Full Stack'],
        ['Semestre', '2023.3'],
        ['Objetivo', 'Missão Certificação'],
        ['Professor', 'ANDRE LUIZ AVELINO SOBRAL'],
        ['Disciplina', 'Projetando uma Aplicação Desktop']
]

SENHA_ACESSO = '123'
USUARIO = 'admin'
SENHA = '123' 

raiz = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(raiz))

# Carrega raiz do projeto
raiz = (sys.path[0])