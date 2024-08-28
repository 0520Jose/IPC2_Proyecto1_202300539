from ListaCircular.Nodo import Nodo
from Listas.Nodo import Nodo as nodo
from Listas.Matriz import Matriz

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
    
    def obtener_lista_binaria(self):
        lista_circular_aux = ListaCircular()

        if self.size == 0:
            print("> No hay nodos en la lista.")
            return

        nodoAux = self.inicio
        while True:
            matrizBinaria = Matriz(nodoAux.m + 1, nodoAux.n + 1)
            for i in range(1, nodoAux.m):
                for j in range(1, nodoAux.n):
                    dato = nodoAux.matriz.obtener_elemento(i, j)
                    if dato == None:
                        pass
                    else:
                        if dato > 0:
                            matrizBinaria.asignar_elemento(i, j, 1)
                        else:
                            matrizBinaria.asignar_elemento(i, j, 0)

            matrizBinaria.mostrar()
            lista_circular_aux.agregarNodo("MatrizBinaria", matrizBinaria, nodoAux.m, nodoAux.n)

            nodoAux = nodoAux.siguiente
            if nodoAux == self.inicio:
                break

        return lista_circular_aux

    
    #def obtener_suma_tuplas():
    #    if lista_circular_aux.size == 0:
    #        print ("> No hay nodos en la lista.")
    #        return
    #    else:
    #       nodoAux = lista_circular_aux.inicio
    #       lista_simple_contenedora = ListaSimple()
    #       for i in range(nodoAux.m):
    #           lista_simple = ListaSimple()
    #           for j in range(nodoAux.n):
    #               dato = nodoAux.matriz[i][j] 
    #               lista_simple.agregarNodo(dato)
    #       lista_simple_contenedora.agregarNodo(lista_simple)
    #       for fila in lista_simple_contenedora:
    #           if fila == fila.siguiente:
    #               print ("Filas iguales")
    #       return
        

