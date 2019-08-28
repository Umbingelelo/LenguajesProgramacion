import re
#FUNCIONES QUE MODIFICAN EL ARCHIVO
def Select(Select_example):

    Select = re.findall(r"SELECT (.+) FROM ([a-zA-Z]*)",Select_example)

    Table = re.findall(r"(\w+|\*)",Select[0][0])

    Inner = re.findall(r"INNER JOIN (\w*)",Select_example)

    Order = re.findall(r"ORDER BY (\w*) (ASC|DESC)",Select_example)

    Where = re.findall(r"(AND|OR)?\s?(\w*)\s?=\s?(\’.+\’|\d*)",Select_example)#problema aca, no encuentra numeros

    print("Se seleccionara: ",Table)
    print("De la tabla: ",Select[0][1])
    print("La lista where: ",Where)
    #print("Ordenado por ",Order[0][0]," By ",Order[0][1])

#---------------------------------------------------------------

def Insert(Insert_example):

    Insert = re.findall(r"INSERT INTO (\w*) \((.*)\) VALUES \((.*)\)",Insert_example)

    Tablas_a_insertar = re.findall(r"\,? (\w*) \,?",Insert[0][1])

    Valores_a_insertar = re.findall(r"(\d+)|\’(.*?)\’",Insert[0][2])#Problema aca, no encuentra las cosas bien, falla en los numeros

    print("La tabla a insertar: ",Insert[0][0])
    print("Los valores a insertar: ",Tablas_a_insertar)
    print("Valores: ",Valores_a_insertar)
#-------------------------------------------------------------------

def Update(Update_example):

    Update = re.findall(r"UPDATE (\w*) SET (.*) WHERE (.*);",Update_example)

    Update_set = re.findall(r"(\w*)\s?=\s?\’?([a-zA-Z\s0-9]*)\’?",Update[0][1])

    Update_where = re.findall(r"(AND|OR)?\s?(\w*)\s?=\s?(\’.+\’|\d*)",Update[0][2]) #Mismo error, los numeros

    print("La tabla a actualizar: ",Update[0][0])
    print("Set: ", Update_set)
    print("Where: ", Update_where,")")

#FUNCIONES QUE REVISAN LA SINTAXIS DE LAS CONSULTAS

def insertSintaxis(example):
    aux=re.fullmatch(r"INSERT INTO (\w+ \(\s\w*(\s,\s\w*)*\s\)) VALUES \(\s(’[a-z-A-Z0-9\s]*’)*(’[a-z-A-Z0-9\s]*’ ,\s?)*(\d*\s?[,\s \)])*;",example)
    if(aux!=None):
        Insert = re.findall(r"INSERT INTO (\w*) \((.*)\) VALUES \((.*)\)",example)
        condiciones_iniciales=Insert[0][1].split(",")
        parametros_dados=Insert[0][2].split(",")
        if(len(condiciones_iniciales)==len(parametros_dados)):
            return True
        else:
            return False
    else:
        return False

def selectSintaxis(example):
    aux = re.fullmatch(r"SELECT (\*|\w+|\,\w+|\w+\,\w+)+ FROM (\w+)\s?(INNER JOIN \w+)?\s?(ORDER BY \w+ (ASC|DESC))?\s?(WHERE ([a-zA-Z0-9]+)\s?=\s?(\'[a-zA-Z0-9\s]+\'|[0-9]+)(\s?(AND|OR) ([a-zA-Z0-9]+)\s?=\s?(\'[a-zA-Z0-9\s]+\'|[0-9]+)\s?)*)?\s?;",example)
    if(aux!=None):
        return True
    return False

def updateSintaxis(example):
    aux = re.fullmatch(r"UPDATE (\w+) SET (\w+\s?=\s?\'[a-zA-Z0-9\s]+\'\s?|\,\w+\s?=\s?\'[a-zA-Z0-9\s]+\'\s?|\s?\w+\s?=\s?[0-9]+\s?|\s?\,\w+\s?=\s?[0-9]+\s?)+ WHERE (([a-zA-Z0-9]+) = (’[a-z-A-Z0-9\s]*’))+\s?(;|((AND|OR) (([a-zA-Z0-9]+) = (’[a-z-A-Z0-9\s]*’))+);)",example)
    if(aux!=None):
        return True
    return False


print("****************Bienvenido al sistema de consultas de Base de Datos SQL*************** \n")
condicion=input("Desea Iniciar la Consulta y/n : )")
if condicion=="y" or condicion == "Y":
    print("Para finalizar la consulta debe ingresar *end* \n")
    while condicion!="end":
        condicion=input("Ingrese consulta \n")
        if re.match(r"SELECT",condicion)!=None:
            if selectSintaxis(condicion):#ahi debe revisar si está bien la sintaxis#ahi debe revisar si está bien la sintaxis
                print("Ingreso funcion SELECT")
                Select(condicion)
            else:
                print("Error de Sintaxis !")
        elif re.match(r"INSERT",condicion)!=None:
            if insertSintaxis(condicion):#ahi debe revisar si está bien la sintaxis
                print("Ingreso funcion INSERT")
                Insert(condicion)
            else:
                print("Error de Sintaxis !")
        elif re.match(r"UPDATE",condicion)!=None:
            if updateSintaxis(condicion):#ahi debe revisar si está bien la sintaxiS
                print("Ingreso funcion UPDATE")
                Update(condicion)
            else:
                print("Error de Sintaxis !")
        elif condicion=="end":
            print ("Fin de la consulta")
        else:
            print("Consulta invalida")
else:
    print("Fin de la consulta")
