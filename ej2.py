#Implementar una función rotateList que tome una lista y un número entero k como
#entrada, y rote la lista k veces hacia la derecha.
#Ejemplo:
#rotateList([1, 2, 3, 4, 5],2) => [4, 5, 1, 2, 3]

def rotateList(list, k):
    k = k % len(list)
    
    parte1 = list[len(list) - k:]
    parte2 = list[:len(list) - k]
    
    list2 = parte1 + parte2
    
    return list2

print(rotateList([1, 2, 3, 4, 5], 2))
