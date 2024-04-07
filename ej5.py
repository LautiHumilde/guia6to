#Escribe una función Scalar que tome dos matrices como entrada y devuelva su
#producto escalar.
#Ejemplo:
#Scalar([[1, 2], [3, 4]],[[2, 0], [1, 2]]) => [[4, 4], [10, 8]]

def Scalar(matriz1, matriz2):
    matriz_nueva = []
    for fila in matriz1:
        fila_resultado = []
        for j in range(len(matriz2[0])):
            producto = sum(fila[k] * matriz2[k][j] for k in range(len(fila)))
            fila_resultado.append(producto)
        matriz_nueva.append(fila_resultado)

    return matriz_nueva

print(Scalar([[1, 2], [3, 4]], [[2, 0], [1, 2]]))
