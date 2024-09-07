from Listas.Nodo_cola import Nodo

class Cola:
    def __init__ (self, posicion, dimension, inicio = None, fin = None, tamaño = 0):
        self.inicio = inicio
        self.fin = fin
        self.tamaño = tamaño
        self.posicion = posicion
        self.dimension = dimension

    def encolar(self, dato, nombre):
        nuevoNodo = Nodo(dato, nombre)
        if self.tamaño == 0:
            self.inicio = nuevoNodo
            self.fin = nuevoNodo
        else:
            self.fin.siguiente = nuevoNodo
            self.fin = nuevoNodo
        self.tamaño += 1

    def desencolar(self):
        if self.inicio is None:
            print("La cola está vacía")
            return None
        else:
            dato = self.inicio.dato
            self.inicio = self.inicio.siguiente
            self.tamaño -= 1
            return dato
        
    def esta_vacia(self):
        if self.tamaño == 0:
            return True

    def imprimirCola(self):
        nodoActual = self.inicio
        while nodoActual != None:
            print(nodoActual.dato, end=" ")
            nodoActual = nodoActual.siguiente

    def imprimirCola_de_colas(self):
        nodoActual = self.inicio
        while nodoActual != None:
            nodoActual.dato.imprimirCola()
            print("")
            nodoActual = nodoActual.siguiente
        print("")