import xml.etree.ElementTree as ET
from xml.dom import minidom
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
            lista_circular.agregarNodo(i.get('nombre'), matriz, filas, columnas)


    def escribirArchivo(self, rutaSalida, archivoProcesado):
        root = ET.Element("matrices")
        
        nodo_actual = archivoProcesado.inicio
        contador = 0
        max_iteraciones = 1000  
        
        while nodo_actual is not None and contador < max_iteraciones:
            matriz_elem = ET.SubElement(root, "matriz")
            matriz_elem.set("nombre", nodo_actual.nombre)
            matriz_elem.set("n", str(nodo_actual.m + 1))
            matriz_elem.set("m", str(nodo_actual.n + 1))
            
            for i in range(nodo_actual.m + 1): 
                for j in range(nodo_actual.n + 1):  
                    dato_elem = ET.SubElement(matriz_elem, "dato")
                    dato_elem.set("x", str(i + 1))
                    dato_elem.set("y", str(j + 1))
                    try:
                        valor = nodo_actual.matriz.obtener_elemento(i, j)
                        dato_elem.text = str(valor)
                    except Exception as e:
                        print(f"Error al obtener elemento ({i},{j}): {e}")
                        dato_elem.text = "0"
            
            if nodo_actual.siguiente == archivoProcesado.inicio:
                break
            nodo_actual = nodo_actual.siguiente
            contador += 1
        
        if contador >= max_iteraciones:
            print("Advertencia: Se alcanzó el límite máximo de iteraciones.")
        
        rough_string = ET.tostring(root, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        pretty_xml = reparsed.toprettyxml(indent="  ")
        
        with open(rutaSalida, "w", encoding="utf-8") as f:
            f.write(pretty_xml)
        
        print(f"Archivo XML escrito exitosamente en {rutaSalida}")
        
    def procesarArchivo(self):
        print ("> Procesando archivo...")
        print ("> Calculando la matriz binaria...")
        lista_binaria = lista_circular.obtener_lista_binaria()
        while not lista_binaria == None:
            nodo_actual = lista_circular.inicio
            lista_de_colas = lista_circular.obtener_colas(nodo_actual)
            lista_respaldo = lista_circular.obtener_colas(nodo_actual)
            print ("> Realizando suma de tuplas...")
            lista_reducida = lista_binaria.obtener_suma_tuplas(lista_de_colas, lista_respaldo)
                
            nodo_actual = nodo_actual.siguiente
                
            if nodo_actual == lista_circular.inicio:
                break
        return lista_reducida

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