archivo = open('archivos/tabla.txt', 'w') 

def tabla_multiplicar():
    numero = int(input('Ingrese un numero: '))
    for i in range(1,11):
        archivo.write(f'{numero} x {i} = {numero*i}\n')
    archivo.close()

tabla_multiplicar()