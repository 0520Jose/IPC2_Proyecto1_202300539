from NodoDato import NodoDato

class ListaSimple:
    def __init__(self, inicio=None, size = 0):
        self.inicio = inicio
        self.size = size

    def agregarNodo(self, dato):
        nuevo_nodo = NodoDato(dato)

        if self.inicio == 0:
            self.inicio = nuevo_nodo
        else:
            nodoAux = self.inicio
            while nodoAux.siguiente:
                nodoAux = nodoAux.siguiente
            nodoAux.siguiente = nuevo_nodo 