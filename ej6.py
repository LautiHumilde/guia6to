#Implementar una función llamada invert que tome un diccionario como entrada y
#devuelva un nuevo diccionario donde las claves sean los valores originales y los
#valores sean listas de las claves originales que tenían ese valor.
#Ejemplo:
#Scalar({'a': 1, 'b': 2, 'c': 1, 'd': 3}) => {1: ['a', 'c'], 2: ['b'], 3:
#['d']}

def invert(dic):
    invertido = {}
    for clave in dic:
        valor = dic[clave]
        if valor in invertido:
            invertido[valor].append(clave)
        else:
            invertido[valor] = [clave]
    return invertido

print(invert({'a': 1, 'b': 2, 'c': 1, 'd': 3}))
