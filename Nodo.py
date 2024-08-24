class Nodo:
    def __init__(self, nombre, matriz, m, n, siguiente = None) -> None:
        self.nombre = nombre
        self.matriz = matriz
        self.siguiente = siguiente
        self.m = m
        self.n = n