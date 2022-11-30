
def lineas(archivo):
    linea = archivo.readline()
    if linea:
        devolver = linea.rstrip("\n").split(",")
    else:
        devolver = ["999", ""]

    return devolver

jugador = "Gaby_005"


archivo_local = open(f"{jugador}.txt")

linea = "esto es una linea de prueba"

archivo_local.write(linea)


archivo_local.close()
