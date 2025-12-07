# Programa 1: Búsqueda en Arreglo Multidimensional


def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j  # Retorna la posición (fila, columna)
    return None

matriz = [
    [10, 25, 37],
    [42, 18, 9],
    [33, 7,  21]
]

print("Matriz:")
for fila in matriz:
    print(fila)

valor_buscar = 18

resultado = buscar_valor(matriz, valor_buscar)

if resultado:
    print(f"\nEl valor {valor_buscar} se encontró en la posición: Fila {resultado[0]}, Columna {resultado[1]}")
else:
    print(f"\nEl valor {valor_buscar} no se encontró en la matriz.")