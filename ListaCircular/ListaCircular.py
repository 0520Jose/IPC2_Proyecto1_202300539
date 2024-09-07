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

            lista_circular_aux.agregarNodo(nodoAux.nombre, matrizBinaria, nodoAux.m, nodoAux.n)

            lista_circular_aux.tamaño += 1
            nodoAux = nodoAux.siguiente
            if nodoAux == self.inicio:
                break

        return lista_circular_aux
    
    def cola_de_colas_a_matriz(self, cola_de_colas):
        if cola_de_colas.tamaño == 0:
            print("> No hay colas en la cola de colas.")
            return
        
        m = cola_de_colas.dimension - 1
        n = cola_de_colas.tamaño - 1 
        print(f"Matriz de {n}x{m}")

        nueva_matriz = Matriz(n, m)
        fila = 0

        while not cola_de_colas.esta_vacia():
            cola_fila = cola_de_colas.desencolar()
            columna = 0

            while not cola_fila.esta_vacia():
                dato = cola_fila.desencolar()
                if fila <= n and columna <= m:
                    nueva_matriz.asignar_elemento(fila, columna, dato)
                columna += 1
            fila += 1

        return nueva_matriz
    
    def obtener_colas(self, nodo_actual):
        if self.tamaño == 0:
            print("> No hay nodos en la lista.")
            return
        
        nodoAux = nodo_actual.matriz
        columna = nodo_actual.m + 1
        fila = nodo_actual.n + 1

        cola_de_colas = Cola(0, columna)
            
        for i in range(fila):
            cola = Cola(i, fila)
                
            for j in range(columna):
                dato = nodoAux.obtener_elemento(i, j)
                cola.encolar(dato, nodo_actual.nombre)
                
            if cola.tamaño == (fila):
                cola_de_colas.encolar(cola, nodo_actual.nombre)
            else:
                print("La cola de la fila no tiene exactamente.")
        return cola_de_colas

    def obtener_suma_tuplas(self, colas_originales, colas_respaldo):
        while not self == None:
            nodo_actual = self.inicio
            cola_de_colas = self.obtener_colas(nodo_actual)
            colas_reducidas = self.compararColas(cola_de_colas, colas_originales, colas_respaldo)
            nodo_actual = nodo_actual.siguiente
                
            if nodo_actual == self.inicio:
                break
        
        matriz = self.cola_de_colas_a_matriz(colas_reducidas)
        lista_circular_reducida = ListaCircular()
        lista_circular_reducida.agregarNodo("MatrizR", matriz, matriz.filas, matriz.columnas)
        
        return lista_circular_reducida
        
        

    def compararColas(self, cola_de_colas, colas_originales, colas_respaldo):
        colas_reducidas = Cola(0, cola_de_colas.dimension)
        colas_respaldo.imprimirCola_de_colas()
        colas_originales.imprimirCola_de_colas()
        cola_de_colas.imprimirCola_de_colas()
        while not cola_de_colas.esta_vacia():
            cola_actual = cola_de_colas.desencolar()
            cola_temporal = Cola(0,0)
            
            while not cola_de_colas.esta_vacia():
                cola_comparar = cola_de_colas.desencolar()
                if cola_comparar is not None:
                    if cola_actual.tamaño == cola_comparar.tamaño:
                        resultado = self.compararNodos(cola_actual, cola_comparar)
                        if resultado:
                            print ("Entro")
                            cola_sumatoria = Cola(0,0)
                            cola_suma = Cola(0, cola_actual.tamaño)

                            while not colas_originales.esta_vacia():
                                print("Entro")
                                cola_original = colas_originales.desencolar()

                                if cola_original.posicion == cola_actual.posicion or cola_original.posicion == cola_comparar.posicion:
                                    print("Entro")
                                    cola_sumatoria.encolar(cola_original, "Original")

                            while not cola_sumatoria.esta_vacia():
                                print("Entro")
                                cola1 = cola_sumatoria.desencolar()
                                cola2 = cola_sumatoria.desencolar()
                                contador = 0
                                if cola1 is not None and cola2 is not None:
                                    while not (cola1.esta_vacia() or cola2.esta_vacia()):
                                        print("Entro")
                                        dato1 = cola1.desencolar()
                                        dato2 = cola2.desencolar()
                                        suma = dato1 + dato2
                                        contador += 1
                                        cola_suma.encolar(suma, str(contador))
                                    cola_suma.imprimirCola()
                                    colas_reducidas.encolar(cola_suma, "reducida")
                                    colas_originales = colas_respaldo
                                    colas_originales.imprimirCola_de_colas()

                                else:
                                    print("Una de las colas es None.")
                    cola_temporal.encolar(cola_comparar, "Temporal")

            while not cola_temporal.esta_vacia():
                encolar = cola_temporal.desencolar()
                cola_de_colas.encolar(encolar, "Cola de colas")
        print ("Fin de la comparación.")
        return colas_reducidas

    def compararNodos(self, cola_actual, cola_comparar):
        nodo_actual = cola_actual.inicio
        nodo_comparar = cola_comparar.inicio
        
        while nodo_actual is not None and nodo_comparar is not None:
            if nodo_actual.dato != nodo_comparar.dato:
                return False
        
            nodo_actual = nodo_actual.siguiente
            nodo_comparar = nodo_comparar.siguiente

        if nodo_actual is None and nodo_comparar is None:  
            print("Todas las tuplas son iguales.")
            return True
        else:
            print("Las colas no son iguales o tienen diferente longitud.")
            return
        
    def imprimir_lista(self):
        if self.tamaño == 0:
            print("> No hay nodos en la lista.")
            return

        nodoAux = self.inicio
        while True:
            print(f"Nombre: {nodoAux.nombre}")
            nodoAux.matriz.imprimir_matriz()
            nodoAux = nodoAux.siguiente
            if nodoAux == self.inicio:
                break

