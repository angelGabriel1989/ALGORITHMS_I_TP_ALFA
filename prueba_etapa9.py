def lineas(archivo):
    linea = archivo.readline()
    if linea:
        devolver = linea.rstrip("\n").split(",")
    else:
        devolver = ["999", ""]

    return devolver


"""Gabriel Barros"""
lista = []
with open("prueba_etapa9.csv") as prueba:
    linea = lineas(prueba)
    max = "999"
        

    while linea[0] != max:
        lista.append((linea[0],int(linea[1])))
        linea = lineas(prueba)


print(lista)



