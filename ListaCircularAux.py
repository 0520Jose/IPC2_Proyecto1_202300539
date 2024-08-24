from NodoAux import NodoAux

class ListaCircularAux:
    def __init__ (self, inicio = None, size = 0) -> None:
        self.inicio = inicio
        self.size = size
    
    def agregarNodo(self, matriz, m, n):
        nuevoNodo = NodoAux(matriz, m, n)

        if self.size == 0:
            self.inicio = nuevoNodo
            self.inicio.siguiente = nuevoNodo
            self.size += 1

        else:
            nodoAux = self.inicio

            while nodoAux.siguiente != self.inicio:
                nodoAux = nodoAux.siguiente
            nodoAux.siguiente = nuevoNodo
            nuevoNodo.siguiente = self.inicio
            self.size += 1