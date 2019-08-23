import re
#FUNCIONES QUE MODIFICAN EL ARCHIVO
def select(texto):
    nombre_a="Estudiantes"#Esta info la debemos sacar de los comandos , ejemplo SELECT FROM NOMBREDELARCHIVO , de ahi lo sacamos
    archivo=open(nombre_a+".csv","w")
    nombre_a.close()
    return True

def insert(texto):
    nombre_a="Estudiantes"#Esta info la debemos sacar de los comandos , ejemplo SELECT FROM NOMBREDELARCHIVO , de ahi lo sacamos
    archivo=open(nombre_a+".csv","w")
    nombre_a.close()
    return True
def update (texto):
    nombre_a="Estudiantes"#Esta info la debemos sacar de los comandos , ejemplo SELECT FROM NOMBREDELARCHIVO , de ahi lo sacamos
    archivo=open(nombre_a+".csv","w")
    nombre_a.close()
    return True

#FUNCIONES QUE REVISAN LA SINTAXIS DE LAS CONSULTAS
def revision_select(texto):
    return True
def revision_insert(texto):
    return True
def revision_update(texto):
    return True

print("****************Bienvenido al sistema de consultas de Base de Datos SQL*************** \n")
condicion=input("Desea Iniciar la Consulta y/n : )")
if condicion=="y" or condicion == "Y":
    print("Para finalizar la consulta debe ingresar *end* \n")
    while condicion!="end":
        condicion=input("Ingrese consulta \n")
        if re.match(r"SELECT",condicion)!=None:
            if revision_select(condicion):#ahi debe revisar si está bien la sintaxis#ahi debe revisar si está bien la sintaxis
                print("Ingreso funcion SELECT")
                select(condicion)
            else:
                print("Error de Sintaxis !")
        elif re.match(r"INSERT",condicion)!=None:
            if revision_insert(condicion):#ahi debe revisar si está bien la sintaxis
                print("Ingreso funcion INSERT")
                insert(condicion)
            else:
                print("Error de Sintaxis !")
        elif re.match(r"UPDATE",condicion)!=None:
            if revision_update(condicion):#ahi debe revisar si está bien la sintaxiS
                print("Ingreso funcion UPDATE")
                update(condicion)   
            else:
                print("Error de Sintaxis !")
        elif condicion=="end":
            print ("Fin de la consulta")
        else:
            print("Consulta invalida")


else:
    print("Fin de la consulta")
