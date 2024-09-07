class Nodo:
    def __init__ (self, dato, nombre, siguiente = None, anterior = None):
        self.dato = dato
        self.nombre = nombre  
        self.siguiente = siguiente
        self.anterior = anterior