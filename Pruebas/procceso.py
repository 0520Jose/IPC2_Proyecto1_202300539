class nodo:
    def __init__ (self, dato):
        self.dato = dato
        self.anterior = None

class fila:
    def __init__ (self):
        self.inicio = None
        self.fin = None
        self.tamaño = 0
    
    def agregar(self, dato):
        nuevoNodo = nodo(dato)
        if self.inicio == None:
            self.inicio = nuevoNodo
            self.fin = nuevoNodo
        else:
            nodoActual = self.fin
            nuevoNodo.anterior = nodoActual
            self.fin = nuevoNodo
        self.tamaño += 1
    
    def sacar(self):
        if self.inicio == None:
            return None
        else:
            nodoActual = self.inicio
            self.inicio = nodoActual.anterior
            return nodoActual.dato




      






        








        



