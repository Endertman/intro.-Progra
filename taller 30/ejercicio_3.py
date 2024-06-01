import numpy as np

def prom_matrix():
    n1 = int(input('Ingrese el tamaño de la matriz: '))
    n2 = int(input('Ingrese el tamaño de la matriz: '))
    matrix1 = np.random.randint(5, size=(n1,n2))
    matrix2 = np.random.randint(5, size=(n1,n2))

    print("Matriz 1:")
    print(matrix1)
    print("\nMatriz 2:")
    print(matrix2)

    promedio1 = sum(sum(row) for row in matrix1) / (n1 * n2)
    print(f'\nEl promedio de la matriz 1 es: {promedio1}')
    promedio2 = sum(sum(row) for row in matrix2) / (n1 * n2)
    print(f'\nEl promedio de la matriz 2 es: {promedio2}')
    promedio = (promedio1 + promedio2) / 2
    print(f'\nEl promedio de los elementos de las matrices es: {promedio}')
    
prom_matrix()