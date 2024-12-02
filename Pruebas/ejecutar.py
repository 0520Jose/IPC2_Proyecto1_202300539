from procceso import fila
import xml.etree.ElementTree as ET
 
datoAnterior = 0


def leerArchivo(entrada):
    global datoAnterior
    arbol = ET.parse(entrada)
    ramas = arbol.getroot()
    for matriz in ramas.iter('matriz'):
        filas = int(matriz.get('m'))
        columnas = int(matriz.get('n'))
        matriz_ = fila()
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
                datoAnterior += 1
               
        

leerArchivo("entrada_.xml")
        
                              









