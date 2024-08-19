def cargarArchivo():
    print ("----------------------------------------------------")
    print ("              Opcion Cargar archivo")
    print ("----------------------------------------------------")
    print ("")
    entrada = input("Ingrese la ruta del archivo: ")
    print ("")
    print ("Archivo cargado exitosamente.")
    print ("")
    print ("")

def procesarArchivo():
    print ("----------------------------------------------------")
    print ("              Opcion Procesar archivo")
    print ("----------------------------------------------------")
    print ("")
    print ("Procesando archivo...")
    print ("Archivo procesado exitosamente.")
    print ("")

def escribirArchivo():
    return

def mostrarDatosEstudiante():
    print ("--------------------------------------------------------------")
    print ("              Opcion Datos del estudiante")
    print ("----------------------------------------------------------------")
    print ("")
    print ("> José Emanuel Monzón Lémus")
    print ("> 2022300539")
    print ("> Introducción a la Programación y Computación 2 Sección 'A'")
    print ("> Ingeniería en Ciencias y Sistemas")
    print ("> 4to. Semestre")
    print ("----------------------------------------------------------------")
    print ("")
    print ("")


def generarGrafica():
    return

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
    eleccion = int(input("Seleccione una opción: "))
    print ("")
    print ("")

    if eleccion == 1:
        cargarArchivo()
    elif eleccion == 2:
        procesarArchivo()
    elif eleccion == 3:
        escribirArchivo()
    elif eleccion == 4:
        mostrarDatosEstudiante()
    elif eleccion == 5:
        generarGrafica()
    elif eleccion == 6:
        print ("Saliendo del programa...")
        break
    else:
        print ("Opción no válida. Intente de nuevo.")
        print ("")
        print ("")
