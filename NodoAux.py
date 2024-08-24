class NodoAux:
    def __init__(self, matriz, m, n, siguiente = None) -> None:
        self.matriz = matriz
        self.siguiente = siguiente
        self.m = m
        self.n = n