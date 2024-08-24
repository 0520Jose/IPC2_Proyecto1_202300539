from Nodo import Nodo
from ListaSimple import ListaSimple

class ListaCircular:
    def __init__ (self, inicio = None, size = 0) -> None:
        self.inicio = inicio
        self.size = size
    
    def agregarNodo(self, nombre, matriz, m, n):
        nuevoNodo = Nodo(nombre, matriz, m, n)

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
    
    def imprimir(self):
        if self.size == 0:
            print ("> No hay nodos en la lista.")
            return
        else:
            nodoAux = self.inicio
            print (f"> {nodoAux.nombre}")
            for fila in nodoAux.matriz:
                print (fila)
            while nodoAux.siguiente != self.inicio:
                nodoAux = nodoAux.siguiente
                print (f"> {nodoAux.nombre}")
                for fila in nodoAux.matriz:
                    print (fila)
            return
        
    def obtener_lista_binaria(self):
        lista_circular_aux = ListaCircular()
        if self.size == 0:
            print ("> No hay nodos en la lista.")
            return
        else:
            nodoAux = self.inicio
            matrizBinaria = [[0 for _ in range(nodoAux.m)] for _ in range(nodoAux.n)]
            for i in range(nodoAux.m):
                for j in range(nodoAux.n):
                    dato = nodoAux.matriz[i][j]
                    if dato > 0:
                        matrizBinaria[i][j] = 1
                    else: 
                        matrizBinaria[i][j] = 0
            lista_circular_aux.agregarNodo(matrizBinaria, nodoAux.m, nodoAux.n)
            for fila in matrizBinaria:
                print (fila)
            while nodoAux.siguiente != self.inicio:
                nodoAux = nodoAux.siguiente
                matrizBinaria = [[0 for _ in range(nodoAux.m)] for _ in range(nodoAux.n)]
                for i in range(nodoAux.m):
                    for j in range(nodoAux.n):
                        dato = nodoAux.matriz[i][j]
                        if dato > 0:
                            matrizBinaria[i][j] = 1
                        else: 
                            matrizBinaria[i][j] = 0
                lista_circular_aux.agregarNodo(matrizBinaria, nodoAux.m, nodoAux.n)
                for fila in matrizBinaria:
                    print (fila)
            return
    def obtener_suma_tuplas():
        if lista_circular_aux.size == 0:
            print ("> No hay nodos en la lista.")
            return
        else:
            nodoAux = lista_circular_aux.inicio
            lista_simple_contenedora = ListaSimple()
            for i in range(nodoAux.m):
                lista_simple = ListaSimple()
                for j in range(nodoAux.n):
                    dato = nodoAux.matriz[i][j] 
                    lista_simple.agregarNodo(dato)
            lista_simple_contenedora.agregarNodo(lista_simple)
            for fila in lista_simple_contenedora:
                if fila == fila.siguiente:
                    print ("Filas iguales")
            return
        

