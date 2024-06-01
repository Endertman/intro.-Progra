# Copiar la informacion de un archivo a otro
def copiarinf():
    with open('ej.txt', 'r') as fichero:
        contenido = fichero.read()
        
    with open('libro.txt', 'w') as fichero_destino:
        fichero_destino.write(contenido)
print("Se está copiando la informacion de un fichero a otro")
copiarinf()

# 2do ejercicio
# escriba un programa que busque una palabra especifica en un fichero llamado libro.txt
# e indique cuantas veces aparece la palabra

def buscarpal():
    palabra=input("Ingrese la palabra a buscar: ")
    with open('ej.txt', 'r') as archivo:
        contenido2 = archivo.read()
    contador = contenido2.count(palabra)
    print(f"la palabra {palabra} aparece {contador} veces.")
buscarpal()

# 3er ejercicio 
# Crear un programa que lea el contenido de un fichero llamado "ej.txt" y lo guarde 
#invertido en un fichero libro.txt

def inv():
    with open('ej.txt', 'r') as archivo_origen:
        conbase = archivo_origen.read()
        
    contenido_invertido = conbase[:: -1]
    with open('libro.txt', 'w') as fichero_destino:
        fichero_destino.write(contenido_invertido)
        
    print("Se está copiando la informacion a la inversa xD")
inv()# Copiar la informacion de un archivo a otro
def copiarinf():
    with open('ej.txt', 'r') as fichero:
        contenido = fichero.read()
        
    with open('libro.txt', 'w') as fichero_destino:
        fichero_destino.write(contenido)
print("Se está copiando la informacion de un fichero a otro")
copiarinf()

# 2do ejercicio
# escriba un programa que busque una palabra especifica en un fichero llamado libro.txt
# e indique cuantas veces aparece la palabra

def buscarpal():
    palabra=input("Ingrese la palabra a buscar: ")
    with open('ej.txt', 'r') as archivo:
        contenido2 = archivo.read()
    contador = contenido2.count(palabra)
    print(f"la palabra {palabra} aparece {contador} veces.")
buscarpal()

# 3er ejercicio 
# Crear un programa que lea el contenido de un fichero llamado "ej.txt" y lo guarde 
#invertido en un fichero libro.txt

def inv():
    with open('ej.txt', 'r') as archivo_origen:
        conbase = archivo_origen.read()
        
    contenido_invertido = conbase[:: -1]
    with open('libro.txt', 'w') as fichero_destino:
        fichero_destino.write(contenido_invertido)
        
    print("Se está copiando la informacion a la inversa xD")
inv()

