import re

def select(texto):
    return 0

def insert(texto):
    return 0
def update (texto):
    return 0

condicion=input("Desea Iniciar la Consulta  y/n: ")
 archivo=input("Ingrese nombre del archivo: \n")+".csv"
if condicion=="y":
    while condicion!="end":
        condicion=input("Ingrese consulta \n")
        if re.match(r"SELECT",condicion)!=None:
            if 1==1:#ahi debe revisar si está bien la sintaxis#ahi debe revisar si está bien la sintaxis
            print("Ingreso funcion SElECT")
            manejo_de_archivo=open(archivo,"r")
            for linea in manejo_de_archivo:
                print(linea)
            manejo_de_archivo.close()
            else:
                print("Error de Sintaxis !")
        elif re.match(r"INSERT",condicion)!=None:
            if 1==1:#ahi debe revisar si está bien la sintaxis
                manejo_de_archivo=open(archivo,"r")
                print("Ingreso funcion INSERT")
                for linea in manejo_de_archivo:
                    print(linea)
            else:
                print("Error de Sintaxis !")

            manejo_de_archivo.close()
        elif re.match(r"UPDATE",condicion)!=None:
            if 1==1:#ahi debe revisar si está bien la sintaxis
                manejo_de_archivo=open(archivo,"r")
                print("Ingreso funcion UPDATE")   
                for linea in manejo_de_archivo:
                    print(linea) 
                manejo_de_archivo.close()
            else:
                print("Error de Sintaxis !")
        else:

    print ("Fin de la consulta")

else:
    print("Fin de la consulta")



"""captura_texto=re.search(r"dab",a)
    if captura_texto != None:
        interprete_texto=captura_texto.group()
print(interprete_texto)"""

"""a="Texto45para78probarlibreria"

b=re.search(r"Te",a)

c=b.group()

print(c)"""