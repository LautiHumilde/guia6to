#Escribe una función sumMatrix que tome dos matrices como entrada y devuelva una
#nueva matriz que sea el resultado de la suma de las dos matrices de entrada. Las
#matrices deben tener la misma dimensión (mismo número de filas y columnas) en
#caso que no lo cumplan se debe avisar al usuario a través de la consola del
#sistema.
#Ejemplo:
#SumMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]],[[9, 8, 7], [6, 5, 4], [3, 2, 1]])
#=> [[10, 10, 10], [10, 10, 10], [10, 10, 10]]

m1 = [
  [5,2,7],
  [8,1,2],
  [9,4,6]
]
m2 = [
  [1,2,3],
  [4,8,6],
  [6,8,9],
]
m3 = [
  [0,0,0],
  [0,0,0],
  [0,0,0]
]

def mult (m1,m2,m3):
  for fila in range(0,len(m1)):
    for colm in range(0,len(m1)):
      m3[fila][colm] = m1[fila][colm] + m2[fila][colm]
  return m3
mult(m1=m1,m2=m2,m3=m3)

print(str(m3[0][0]) + " " + str(m3[0][1]) + " " + str(m3[0][2]))
print(str(m3[1][0]) + " " + str(m3[1][1]) + " " + str(m3[1][2]))
print(str(m3[2][0]) + " " + str(m3[2][1]) + " " + str(m3[2][2]))
