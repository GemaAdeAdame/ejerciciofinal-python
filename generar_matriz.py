import numpy as np

def generar_matriz(N):
    """
    Genera una matriz cuadrada de tamaño NxN y la llena con números aleatorios entre 0 y 9.
    """
    matriz = np.random.randint(0, 10, size=(N, N))
    return matriz

def calcular_sumas(matriz):
    """
    Calcula la suma de los elementos de cada fila y columna de la matriz y las almacena en dos listas.
    """
    sumas_filas = np.sum(matriz, axis=1)
    sumas_columnas = np.sum(matriz, axis=0)
    return sumas_filas, sumas_columnas

try:
    N = int(input("Ingrese el valor de N para generar la matriz: "))
    if N <= 0:
        raise ValueError
except ValueError:
    print("El valor de N debe ser un número entero positivo.")
else:
    
    matriz = generar_matriz(N)
    print("Matriz generada:")
    for fila in matriz:
        print(fila)
    
    sumas_filas, sumas_columnas = calcular_sumas(matriz)
    
    print("Suma de cada fila:")
    for i, suma in enumerate(sumas_filas):
        print(f"Fila {i+1}: {suma}")
    
    print("Suma de cada columna:")
    for i, suma in enumerate(sumas_columnas):
        print(f"Columna {i+1}: {suma}")

# Pruebas unitarias 
assert len(matriz) == N, "Error! La matriz generada no tiene el tamaño correcto"
assert len(sumas_filas) == N, "Error! La cantidad de sumas de filas es incorrecta"
assert len(sumas_columnas) == N, "Error! La cantidad de sumas de columnas es incorrecta"
assert sum(sumas_filas) == np.sum(matriz), "Error! La suma total de filas es incorrecta"
assert sum(sumas_columnas) == np.sum(matriz), "Error! La suma total de columnas es incorrecta"

print("Superadas las pruebas unitarias")
