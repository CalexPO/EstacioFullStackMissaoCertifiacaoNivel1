import PySimpleGUI as sg
import os, sys
from banco.conexao import database

# Inicia classe banco conexão
db = database()

def validaMatriz(codigoUsuario, codigoPerfil):

    # Lista PerfilUsuario
    ListaPerfilUsuario = db.selectValues(f"PerfilUsuario", codigoUsuario, "")

    lista1 = []
    
    # Adiciona à lista o códido do NOVO perfil usuário digitado na tela
    lista1.append(codigoPerfil)
    
    for i in ListaPerfilUsuario:
        campo = i[1]
        lista1 += [campo]
    
    ListaMatrizSoD = db.selectValues(f"MatrizSoD", codigoUsuario, "")
    
    # Lista Primeiro perfil definido na Matriz
    listaM1 = []
    for i in ListaMatrizSoD:
        campo = i[0]
        listaM1 += [campo]

    # Lista segundo perfil definido na Matriz
    listaM2 = []
    for i in ListaMatrizSoD:
        campo = i[1]
        listaM2 += [campo]

    # Verifica se o perfil digitado existe na Matriz (Perfil 1 e Perfil 2)                        
    if (len([elemento for elemento in lista1 if elemento in listaM1])) > 0 and (len([elemento for elemento in lista1 if elemento in listaM2])) > 0:
        connflito1 = set([elemento for elemento in lista1 if elemento in listaM1])
        connflito2 = set([elemento for elemento in lista1 if elemento in listaM2]) 

        # Carrega Perfil 1 em conflito
        ls1 = []
        for i in connflito1:
            ls1 = i

        # Carrega Perfil 2 em conflito            
        ls2 = []
        for i in connflito2:
            ls2 = i

        mensagem = db.selectValues(f"MatrizSoDMensagem", ls1, ls2)
        
        return 'conflito', mensagem

    else:
        return 'naoconflito', ''
        
def valida_cpf(cpf):
    
    # Remove caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = 0
    peso = 10
    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    # Calcula o segundo dígito verificador
    soma = 0
    peso = 11
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    # Verifica se os dígitos verificadores calculados são iguais aos do CPF
    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
        return True
    else:
        return False

def format_cpf(cpf):
    
    for i in enumerate(cpf):

        print(cpf)
        if len(cpf) == 3:
            cpf = cpf[:3] + "." + cpf[3:]
            print('\n', cpf)
        
        if len(cpf) == 7:
            cpf = cpf[:7] + "." + cpf[7:]
            print('\n', cpf)
        
        if len(cpf) == 11:
            cpf = cpf[:11] + "-" + cpf[11:]
            print('\n', cpf)
            
        if len(cpf) > 14:
            return cpf[:14]
                    
        return cpf
    