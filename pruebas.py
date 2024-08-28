from Listas.Matriz import Matriz
# Crear una matriz de 3x3
m = Matriz(3, 3)

# Asignar valores
m.asignar_elemento(0, 0, 5)
m.asignar_elemento(1, 1, 10)
m.asignar_elemento(2, 2, 15)

# Obtener y mostrar valores
print(m.obtener_elemento(0, 0))  # 5
print(m.obtener_elemento(1, 1))  # 10
print(m.obtener_elemento(2, 2))  # 15

# Mostrar la matriz completa
m.mostrar()
