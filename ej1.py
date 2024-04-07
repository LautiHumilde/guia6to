#Implementar una función partList que tome una lista y un número entero k como
#entrada, y devuelva una lista donde todos los elementos menores que k aparezcan
#antes de los elementos mayores o iguales que k, manteniendo el orden relativo de
#los elementos.
#Ejemplo:
#partList([4, 3, 2, 1, 5, 6] ,4) => [3, 2, 1, 4, 5, 6]

def partList (list,k):
    listord = []
    
    for i in range(0,len(list)):
        if list[i] < k:
            listord.append(list[i])

    for i in range(0,len(list)):
        if list[i] >= k:
            listord.append(list[i])
    return listord

print(partList([4, 3, 2, 1, 5, 6] ,4))