#se cuentan del 0 al 9, recordar indice 0-9, posicion 1-infinito, elemento 1-infinito
#lista permite modificacion de variables
lista = ["Endert Guerrero","Endert_man",True,1.60]

#tupla no permite modificaciones
tupla = ("Endert Guerrero","Endert_man",True,1.60)

#tupla[3] = "maquinaria"

#valido solo para lista
lista[3] = "elpepe"

#crear un conjunto (set), no tiene un orden fijo, son desordenado, pueden intercambiar su posicion, pero no se pueden modificar sus elementos, tampoco permite acceder por indice ej: print(conjunto[1]), no permite repetir valores, para acceder a sus datos se hace por un bucle
conjunto = {"Endert Guerrero","Endert_man",True,1.60}
#conjunto[3] = "elpepe" no funciona

#creando un diccionario (dict)
diccionario = {
    "nombre" : "Endert Guerrero",
    "alias" : "Endertman",
    "esta_programando" : True,
    "altura" : 1.70,
    "dato_duplicado" : "Endert Guerrero"
    #key/valor : valor
}

#permite cambios
diccionario["alias"] = "elpepe"

 
print(lista)
print(lista[1])
print(tupla)
print(tupla[0])
print(conjunto)
#print(conjunto)no funciona
print(diccionario)
print(diccionario["alias"])
#modificacion de valores
print(diccionario["altura"] + 2)   


