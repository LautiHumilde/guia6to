#Implementar una función llamada averageKeys que tome un diccionario donde los
#valores son listas de números y devuelva un nuevo diccionario donde los valores
#sean los promedios de las listas correspondientes.
#Ejemplo:
#averageKeys({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}) => {'a': 2.0,
#'b':5.0, 'c': 8.0}

def averageKeys(diccionario):
    promedios = {}
    for clave in diccionario:
        numeros = diccionario[clave]
        promedio = sum(numeros) / len(numeros)
        promedios[clave] = promedio
    return promedios

print(averageKeys({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}))

