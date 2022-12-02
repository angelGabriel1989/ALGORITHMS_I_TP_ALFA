def leerlinea(archivo):
    linea = archivo.readline()
    if linea:
        devolver = linea.rstrip("\n").split(",")
    else:
        devolver = ["999","0"]

    return devolver

def imprimir_archivo():
    archivo = open("01- borrador_prueba.csv")
    
    pos, nombre = leerlinea(archivo)

    max = "999"

    while pos != max:
        print(f"{pos} {nombre}")
        pos, nombre = leerlinea(archivo)

    archivo.close()


def main():
    imprimir_archivo()
    imprimir_archivo()



main()