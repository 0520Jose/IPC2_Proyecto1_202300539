import xml.etree.ElementTree as ET
from globales import lista_circular
from Listas.Matriz import Matriz

class archivoXML:
    def leerArchivo(self, entrada):
        arbol = ET.parse(entrada)
        ramas = arbol.getroot()

        for i in ramas.iter('matriz'):
            filas = int(i.get('m')) - 1
            columnas = int(i.get('n')) - 1
            matriz = Matriz(filas, columnas) 

            for j in i.iter('dato'):
                x = int(j.get('x')) - 1
                y = int(j.get('y')) - 1 
                dato = int(j.text)

                matriz.asignar_elemento(x, y, dato)
            matriz.mostrar()
            lista_circular.agregarNodo(i.get('nombre'), matriz, filas, columnas)


    def escribirArchivo(self, rutaSalida, archivoProcesado):
        arbol = ET.Element("matrices")
        rama = ET.SubElement(arbol, "matriz")
        for i in range(1, 16):
            ET.SubElement(rama, "dato", x=str(i), y=str(i)).text=str(archivoProcesado)
        arbolSalida = ET.ElementTree(arbol)
        ET.dump(arbolSalida)
        self.indentar(arbol)
        try:
            arbolSalida.write(rutaSalida)
        except:
            print ("> Error. No se pudo escribir el archivo.")
        else:
            return
        
    def procesarArchivo(self):
        print ("> Procesando archivo...")
        print ("> Calculando la matriz binaria...")
        lista_binaria = lista_circular.obtener_lista_binaria()
        print ("> Realizando suma de tuplas...")
        lista_binaria.obtener_suma_tuplas()
        print ("> Archivo procesado exitosamente.")

    def indentar(self, elemento, nivel=0, horizontal='\t', vertical='\n'):
        i = vertical + nivel * horizontal
        if len(elemento):
            if not elemento.text or not elemento.text.strip():
                elemento.text = i + horizontal
            if not elemento.tail or not elemento.tail.strip():
                elemento.tail = i
            for elemento in elemento:
                self.indentar(elemento, nivel + 1, horizontal, vertical)
            if not elemento.tail or not elemento.tail.strip():
                elemento.tail = i
        else:
            if nivel and (not elemento.tail or not elemento.tail.strip()):
                elemento.tail = i