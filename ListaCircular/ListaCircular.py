from ListaCircular.Nodo import Nodo
from Listas.Matriz import Matriz
from Listas.Cola import Cola

class ListaCircular:
    def __init__ (self, inicio = None, tamaño = 0) -> None:
        self.inicio = inicio
        self.tamaño = tamaño
    
    def agregarNodo(self, nombre, matriz, m, n):
        nuevoNodo = Nodo(nombre, matriz, m, n)

        if self.tamaño == 0:
            self.inicio = nuevoNodo
            self.inicio.siguiente = nuevoNodo
            self.tamaño += 1

        else:
            nodoAux = self.inicio

            while nodoAux.siguiente != self.inicio:
                nodoAux = nodoAux.siguiente
            nodoAux.siguiente = nuevoNodo
            nuevoNodo.siguiente = self.inicio
            self.tamaño += 1
    
    def obtener_lista_binaria(self):
        lista_circular_aux = ListaCircular()
        if self.tamaño == 0:
            print("> No hay nodos en la lista.")
            return

        nodoAux = self.inicio
        while True:
            columa = nodoAux.m + 1
            fila = nodoAux.n + 1
            matrizBinaria = Matriz(nodoAux.m, nodoAux.n)
            for i in range(columa):
                for j in range(fila):
                    dato = nodoAux.matriz.obtener_elemento(i, j)
                    if dato > 0:
                        matrizBinaria.asignar_elemento(i, j, 1)
                    else:
                        matrizBinaria.asignar_elemento(i, j, 0)

            matrizBinaria.mostrar()
            lista_circular_aux.agregarNodo("MatrizBinaria", matrizBinaria, nodoAux.m, nodoAux.n)

            lista_circular_aux.tamaño += 1
            nodoAux = nodoAux.siguiente
            if nodoAux == self.inicio:
                lista_circular_aux.tamaño += 1
                break

        return lista_circular_aux
    
    def obtener_suma_tuplas(self):
        if self.tamaño == 0:
            print("> No hay nodos en la lista.")
            return
        
        cola_de_colas = Cola()
        nodo_actual = self.inicio
        
        while True:
            nodoAux = nodo_actual.matriz
            columna = nodo_actual.m + 1
            fila = nodo_actual.n + 1
            
            for i in range(fila):
                cola = Cola()
                
                for j in range(columna):
                    dato = nodoAux.obtener_elemento(i, j)
                    cola.encolar(dato)
                
                if cola.tamaño == (fila + 1):
                    cola_de_colas.encolar(cola)
                else:
                    print("La cola de la fila no tiene exactamente.")
            
            nodo_actual = nodo_actual.siguiente
            
            if nodo_actual == self.inicio:
                break

        self.compararColas(cola_de_colas)

    def compararColas(self, cola_de_colas):
        while not cola_de_colas.esta_vacia():
            cola_actual = cola_de_colas.desencolar()
            cola_temporal = Cola()
            cola_temporal_comparados = Cola()
            
            while not cola_de_colas.esta_vacia():
                cola_comparar = cola_de_colas.desencolar()
                if cola_actual.tamaño == cola_comparar.tamaño:
                    print("Cola Actual:")
                    cola_actual.imprimirCola()
                    print("_______________")
                    print("Cola a Comparar:")
                    cola_comparar.imprimirCola()
                    print("_______________")
                    self.compararNodos(cola_actual, cola_comparar)                
                cola_temporal.encolar(cola_comparar)
                cola_temporal.imprimirCola_de_colas()

            while not cola_temporal.esta_vacia():
                cola_de_colas.encolar(cola_temporal.desencolar())

            cola_temporal_comparados.encolar(cola_actual)





    def compararNodos(self, cola_actual, cola_comparar):
        nodo_actual = cola_actual.inicio
        nodo_comparar = cola_comparar.inicio
        
        while nodo_actual is not None and nodo_comparar is not None:
            if nodo_actual.dato != nodo_comparar.dato:
                print(f"({nodo_actual.dato}, {nodo_comparar.dato}) son diferentes")
                return
            else:
                print(f"({nodo_actual.dato}, {nodo_comparar.dato}) son iguales")
        
            nodo_actual = nodo_actual.siguiente
            nodo_comparar = nodo_comparar.siguiente

        if nodo_actual is None and nodo_comparar is None:
            print("Todas las tuplas son iguales.")
            return cola_actual, cola_comparar
        else:
            print("Las colas no son iguales o tienen diferente longitud.")
            return

    
    def mostrarLista(self):
        if self.tamaño == 0:
            print("> No hay nodos en la lista.")
            return
        nodoAux = self.inicio
        while True:
            print(f"Nombre: {nodoAux.nombre}")
            nodoAux.matriz.mostrar()
            nodoAux = nodoAux.siguiente
            if nodoAux == self.inicio:
                break
        print("")

