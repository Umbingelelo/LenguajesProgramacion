import re

reserved = {
	'mientras' : 'WHILE',
	'si_no' : 'ELSE',
	'para_cada' : 'FOR',
	'en' : 'IN',
	'si' : 'IF',
	'fin' : 'FIN',
	'var' : 'VAR',
	'procedimiento' : 'PROC',
	'preguntar' : 'ASK',
	'imprimir' : 'PRINT',
	'retornar' : 'RETURN',
	'entonces' : 'ENTONCES'
}

def INICICIO(palabra):
    return 0

def ciclo_WHILE(palabra):
    return 0

def condicional_IF(palabra):
    return 0
def condicional_ELSE(palabra):
    return 0

def booleano_AND(palabra):
    return 0

def booleano_OR(palabra):
    return 0

def booleano_NO(palabra):
    return 0

def booleano_EQUAL_TO(palabra):
    return 0

def booleano_DIFFERENT_TO(palabra):
    return 0
def booleano_GREATER(palabra):
    return 0
def booleano_SMALLER(palabra):
    return 0






archivo=open("pseudocode.txt","r")
for linea in archivo:
    a=linea.strip()
    captura_texto=re.search(r"dab",a)
    if captura_texto != None:
        interprete_texto=captura_texto.group()
        print(interprete_texto)
    
    
    
    #print (linea.strip())
archivo.close()



"""texto_prueba="345hola456como345estas900"

captura_texto=re.search(r"\d\d\d",texto_prueba)
if captura_texto != None:
    interprete_texto=captura_texto.group()
    print(interprete_texto)"""
