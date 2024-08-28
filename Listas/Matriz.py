from Listas.Nodo import Nodo
class Matriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.inicio = self.crear_matriz(filas, columnas)

    def crear_matriz(self, filas, columnas):
        # Crear la primera fila de nodos
        fila_actual = Nodo()
        fila_inicio = fila_actual
        for _ in range(columnas):
            fila_actual.derecha = Nodo()
            fila_actual = fila_actual.derecha

        # Conectar el resto de las filas
        fila_superior = fila_inicio
        for _ in range(filas):
            fila_actual = Nodo()
            fila_superior.abajo = fila_actual
            fila_superior = fila_superior.abajo
            fila_actual_inicio = fila_actual
            for _ in range(columnas):
                fila_actual.derecha = Nodo()
                fila_actual = fila_actual.derecha
                fila_superior.derecha.abajo = fila_actual
                fila_superior = fila_superior.derecha
            fila_superior = fila_actual_inicio

        return fila_inicio

    def obtener_nodo(self, i, j):
        nodo_actual = self.inicio
        for _ in range(i):
            if nodo_actual.abajo:
                nodo_actual = nodo_actual.abajo
            else:
                raise IndexError("Índice fuera de rango")
        for _ in range(j):
            if nodo_actual.derecha:
                nodo_actual = nodo_actual.derecha
            else:
                raise IndexError("Índice fuera de rango")
        return nodo_actual

    def obtener_elemento(self, i, j):
        nodo = self.obtener_nodo(i, j)
        return nodo.valor

    def asignar_elemento(self, i, j, valor):
        nodo = self.obtener_nodo(i, j)
        nodo.valor = valor

    def mostrar(self):
        nodo_fila = self.inicio
        while nodo_fila:
            nodo_actual = nodo_fila
            fila = []
            while nodo_actual:
                fila.append(str(nodo_actual.valor))
                nodo_actual = nodo_actual.derecha
            print(" ".join(fila))
            nodo_fila = nodo_fila.abajo

    
    # 
