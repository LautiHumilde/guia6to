#Implementa una función mixDict que tome dos diccionarios como entrada y devuelva
#un nuevo diccionario que contenga todas las claves de ambos diccionarios y sus
#valores correspondientes. Si hay claves duplicadas, suma los valores.
#Ejemplo:
#mixDict({'a':1, 'b':2, 'c':3},{'b':3, 'c':4, 'd':5})=>{'a':1, 'b':5,'c': 7, 'd': 5}

def mixDict(dic1, dic2):
    result = {}

    for clave in dic1:
        if clave in result:
            result[clave] += dic1[clave]
        else:
            result[clave] = dic1[clave]

    for clave in dic2:
        if clave in result:
            result[clave] += dic2[clave]
        else:
            result[clave] = dic2[clave]

    return result

print(mixDict({'a': 1, 'b': 2, 'c': 3}, {'b': 3, 'c': 4, 'd': 5}))
