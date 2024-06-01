import numpy as np
def vectores():
    n = int(input("Ingrese el tamaño del vector: \n"))
    v1 = []
    v2 = []

    print('Ingrese los valores de vector 1')
 
    for i in range(n):
        v1.append(int(input(f"Vector 1: Ingrese el valor {i+1}, restan {((i+1)-n)*-1} numeros por ingresar: \n")))

    print('Ingrese los valores de vector 2 \n')

    for i in range(n): 
        v2.append(int(input(f"Vector : Ingrese el valor {i+1}, restan {((i+1)-n)*-1} numeros por ingresar: \n")))4
        

    for i in range(n):
        t2 = []
        t2.append(v1[i]+v2[i])
        print(t2)

    for i in range(n):
        t3 = []
        t3.append(v1[i]-v2[i])
        print(t3)

    for i in range(n):
        t1 = []
        t1.append(v1[i]*v2[i])
        print(t1)

    for i in range(n):
        t4 = []
        t4.append(v1[i]/v2[i])
        print(t4)

vectores()