class nodo:
    def __init__ (self, dato, x, y):
        self.dato = dato
        self.siguiente = None
        self.x = None
        self.y = None

class fila:
    def __init__ (self):
        self.inicio = None
        self.fin = None
        self.tamaño = 0
    
    def agregar(self, dato, x, y):
        nuevoNodo = nodo(dato, x, y)
        if self.inicio == None:
            self.inicio = nuevoNodo
            self.fin = nuevoNodo
        else:
            nodoActual = self.fin
            nodoActual.siguiente = nuevoNodo
            self.fin = nuevoNodo
        self.tamaño += 1
    
    def sacar(self):
        if self.inicio == None:
            return None
        else:
            nodoAux = self.inicio.siguiente
            nodoActual = self.inicio
            self.inicio = nodoAux
            return nodoActual.dato

    def imprimir(self):
        nodoActual = self.inicio
        while nodoActual != None:
            print(nodoActual.dato, end=' ')
            nodoActual = nodoActual.siguiente
    
    def imprimirFilas(self):
        nodoActual = self.inicio
        while nodoActual != None:
            nodoActual.dato.imprimir()
            print("")
            nodoActual = nodoActual.siguiente



      






        








        



