from procceso import fila

fila = fila()
fila.agregar(1)
fila.agregar(2)
fila.agregar(3)

while fila.tamaño > 0:
    print(fila.sacar())
    fila.tamaño -= 1