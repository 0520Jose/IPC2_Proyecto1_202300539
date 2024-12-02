from archivoXML import archivoXML
from graficar import Reportes
from ListaCircular.ListaCircular import ListaCircular
class opcionesPrincipales:
    def __init__(self):
        self.archivo = archivoXML()
        self.archivoLeido = None
        self.archivoProcesado = None
        self.lista_reducida = None

    def cargarArchivo(self):
        print ("----------------------------------------------------")
        print ("              Opcion Cargar archivo")
        print ("----------------------------------------------------")
        print ("")
        try:
            entrada = input("> Ingrese la ruta del archivo: ")
            self.archivoLeido = self.archivo.leerArchivo(entrada)
        except Exception as e:
            print("> Error. No se pudo cargar el archivo.")
            print(f"> Detalles del error: {e}")
            print("")
            print("")
            self.cargarArchivo()
        else:
            print("")
            print("> Se cargo el archivo satisfactoriamente.")
            print("")
            print("")

    def procesarArchivo(self):
        print ("----------------------------------------------------")
        print ("              Opcion Procesar archivo")
        print ("----------------------------------------------------")
        print ("")
        print ("> Procesando archivo...")
        lista_reducida = self.archivo.procesarArchivo()
        if self.archivoProcesado == None:
            print ("> Archivo procesado exitosamente.")
            print ("")
            return lista_reducida
        else:
            self.procesarArchivo()

    def escribirArchivo(self):
        print ("----------------------------------------------------")
        print ("              Opcion Escribir archivo")
        print ("----------------------------------------------------")
        print ("")
        rutaSalida = input("> Ingresar una ruta especifica: ")
        print ("> Escribiendo archivo...")
        archivo = archivoXML()
        archivo.escribirArchivo(rutaSalida, self.lista_reducida)
        print ("> Archivo escrito exitosamente.")

    def mostrarDatosEstudiante(self):
        print ("--------------------------------------------------------------")
        print ("              Opcion Datos del estudiante")
        print ("----------------------------------------------------------------")
        print ("")
        print ("> José Emanuel Monzón Lémus")
        print ("> 2022300539")
        print ("> Introducción a la Programación y Computación 2 Sección 'A'")
        print ("> Ingeniería en Ciencias y Sistemas")
        print ("> 4to. Semestre")
        print ("> Link al repositorio: [https://github.com/tu_usuario/tu_repositorio]")
        print ("----------------------------------------------------------------")
        print ("")
        print ("")

    def generarGrafica(self):
        print ("----------------------------------------------------")
        print ("              Opcion Generar gráfica")
        print ("----------------------------------------------------")
        print ("")
        self.lista_reducida.imprimir_lista()
        Reportes.graficar(self.lista_reducida)
        print ("> Gráfica generada exitosamente.")
        print ("")
        print ("")
        

    def menuPrincipal(self):
        while True:
            print ("----------------------------------------------------")
            print ("                  Menú principal")
            print ("----------------------------------------------------")
            print ("1. Cargar archivo")
            print ("2. Procesar archivo")
            print ("3. Escribir archivo de salida")
            print ("4. Mostrar datos del estudiante")
            print ("5. Generar gráfica")
            print ("6. Salir")
            print ("----------------------------------------------------")
            print ("")
            eleccion = int(input("> Seleccione una opción: "))
            print ("")
            print ("")

            if eleccion == 1:
                self.cargarArchivo()
            elif eleccion == 2:
                self.lista_reducida = self.procesarArchivo()
            elif eleccion == 3:
                self.escribirArchivo()
            elif eleccion == 4:
                self.mostrarDatosEstudiante()
            elif eleccion == 5:
                self.generarGrafica()
            elif eleccion == 6:
                print ("> Saliendo del programa...")
                break
            else:
                print ("> Opción no válida. Intente de nuevo.")
                print ("")
                print ("")
                self.menuPrincipal()
opcionesPrincipales().menuPrincipal()