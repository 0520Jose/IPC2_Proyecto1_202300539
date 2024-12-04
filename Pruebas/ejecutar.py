from procceso import fila
from ListaCircular import ListaCircular
import xml.etree.ElementTree as ET
 
datoAnterior = 0
fila1 = None
listaCircular = ListaCircular()
filas = fila()


def leerArchivo(entrada):
    global datoAnterior, fila1, listaCircular
    arbol = ET.parse(entrada)
    ramas = arbol.getroot()
    for matriz in ramas.iter('matriz'):
        filas = int(matriz.get('m'))
        columnas = int(matriz.get('n'))
        matriz_ = fila()
        nombre = matriz.get('nombre')
        for dato in matriz.iter('dato'):

            x = int(dato.get('x'))
            y = int(dato.get('y'))

            dato_ = int(dato.text)
            if datoAnterior == x: 

                fila1.agregar(dato_, x, y)
            else:
                if fila1 != None:
                    matriz_.agregar(fila1, 0, 0)
                fila1 = fila()
                fila1.agregar(dato_, x, y)
                datoAnterior += 1
        matriz_.agregar(fila1, 0, 0)
        listaCircular.agregarNodo(nombre, matriz_, filas,  columnas)

def listaBinaria(listaCircular):

    matriz = listaCircular.inicio
    
    #while matriz.siguiente != listaCircular.inicio:
    obtenerBinaria(matriz.matriz)
    compararFilas(matriz.matriz)



    #matriz = matriz.siguiente
       
def obtenerBinaria(matriz):
    fila = matriz.inicio

    while fila:
        dato = fila.dato.inicio
        while dato:

            if int(dato.dato) > 0:

                dato.dato = 1
            dato = dato.siguiente
        fila = fila.siguiente
                              
def compararFilas(matriz):
    global filas
    posicionFila = 1
    posicionFila2 = 1 

    fila = matriz.inicio
    while fila:
        fila2 = fila.siguiente
        while fila2:

            dato = fila.dato.inicio
            dato2 = fila2.dato.inicio

            while dato and dato2:
                if dato.dato == dato2.dato:
                    dato = dato.siguiente
                    dato2 = dato2.siguiente
                    filas.agregar("iguales", posicionFila, posicionFila2)
                    posicionFila += 1
                    posicionFila2 += 1
                else:
                    print("No son iguales")
                    dato = None
                    dato2 = None
 
            fila2 = fila2.siguiente
        fila = fila.siguiente
            


leerArchivo("entrada_.xml")
listaBinaria(listaCircular)
listaCircular.imprimir_lista()
filas.imprimir()









