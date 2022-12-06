def leer_linea(archivo, default):
    linea = archivo.readlines()
    return linea.rstrip("\n").split(",")if linea else default

def generar_diccionario(lista):
    diccionario = {}
    for palabra in lista:
        if palabra not in diccionario:
            diccionario[palabra]=1
        else:
            diccionario[palabra]+=1
    return sorted(diccionario.items(),key = lambda item:item[0])

def filtrador_de_palabras(archivo_texto,default):
    archivo = open(archivo_texto)
    linea = leer_linea(archivo_texto,default)
    lista_palabras = []
    while linea:
        for posicion in linea:
            palabra = linea[posicion]
            #Aplano la palabra
            palabra = eliminar_acentuados(palabra)
            if palabra.isalpha():
                lista_palabras.append(palabra.lower())
        linea = leer_linea(archivo_texto)
    archivo.close()
    return lista_palabras
    
def eliminar_acentuados(cadena):
    caracteres_acentuados = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in caracteres_acentuados:
        cadena = cadena.replace(a, b).replace(a.upper(), b.upper())
    return cadena


def palabras_a_jugar(archivo1, archivo2, archivo3, archivo4):
    
    listado_palabras_archivo1 = []
    listado_palabras_archivo2 = []
    listado_palabras_archivo3 = []

    listado_palabras_a_jugar = []

    variable_control_archivo1 = True
    while variable_control_archivo1:
        palabras_arc1 = filtrador_de_palabras(archivo1)
        listado_palabras_archivo1 = generar_diccionario(palabras_arc1)
        variable_control_archivo1 = False
    
    variable_control_archivo2 = True
    while variable_control_archivo2:
        
        palabras_arc2 = filtrador_de_palabras(archivo2)
        listado_palabras_archivo2 = generar_diccionario(palabras_arc2)
        variable_control_archivo2 = False

    variable_control_archivo3 = True
    while variable_control_archivo3:
        
        palabras_arc3 = filtrador_de_palabras(archivo3)
        listado_palabras_archivo3 = generar_diccionario(palabras_arc3)
        variable_control_archivo3 = False
    
    for sublista in listado_palabras_archivo1:
        if sublista[0] not in listado_palabras_a_jugar:
            listado_palabras_a_jugar.append(sublista[0])
    
    for sublista in listado_palabras_archivo2:
        if sublista[0] not in listado_palabras_a_jugar:
            listado_palabras_a_jugar.append(sublista[0])
    
    for sublista in listado_palabras_archivo3:
        if sublista[0] not in listado_palabras_a_jugar:
            listado_palabras_a_jugar.append(sublista[0])

    archivo1.close()
    archivo2.close()
    archivo3.close()

    #Solo queda abierto archivo_4 -> "palabras.txt"

    # ---------------------- "APAREO" ----------------------------------- #
    long_archivo1 = len(listado_palabras_archivo1)-1
    long_archivo2 = len(listado_palabras_archivo2)-1
    long_archivo3 = len(listado_palabras_archivo3)-1

    lista_variables_corte_control = [0,0,0]
    while lista_variables_corte_control[0] <= long_archivo1 and lista_variables_corte_control[1]<= long_archivo2 and lista_variables_corte_control[2]<= long_archivo3:
        #Defino variables que van a almacenar las veces que se repiten las palabras en cada archivo
        acumulador_pal_arc1 = 0
        acumulador_pal_arc2 = 0
        acumulador_pal_arc3 = 0
        minimo = min(listado_palabras_archivo1[lista_variables_corte_control[0]][0],listado_palabras_archivo2[lista_variables_corte_control[1]][0],palabras_archivo3[lista_variables_corte_control[2]][0])
        #Comienza a contar cuantas veces se repite la palabra en los 3 archivo
        while listado_palabras_archivo1[lista_variables_corte_control[0]] == minimo and lista_variables_corte_control[0]==long_archivo1:
            acumulador_pal_arc1 = int(listado_palabras_archivo1[lista_variables_corte_control[1]])
            lista_variables_corte_control[0] +=1
        while listado_palabras_archivo2[lista_variables_corte_control[1]] == minimo and lista_variables_corte_control[1]==long_archivo1:
            acumulador_pal_arc1 = int(listado_palabras_archivo2[lista_variables_corte_control[1]])
            lista_variables_corte_control[1] +=1
        while listado_palabras_archivo1[lista_variables_corte_control[2]] == minimo and lista_variables_corte_control[2]==long_archivo1:
            acumulador_pal_arc1 = int(listado_palabras_archivo3[lista_variables_corte_control[1]])
            lista_variables_corte_control[2] +=1
        #Una vez termine de contar cuantas veces se repite la palabra en cada archivo lo escribe en archivo_4
        archivo4.append(str(minimo) + "," + str(acumulador_pal_arc1) + ","+ str(acumulador_pal_arc2) +  "," + str(acumulador_pal_arc3) + "\n")
    archivo4.close()
    return palabras_a_jugar

def main():
    default = '999999'
    archivo_1 = open ("Cuentos.txt", "r")
    archivo_2 = open ("La araña negra - tomo 1.txt", "r")
    archivo_3 = open ("Las 1000 Noches y 1 Noche.txt", "r")
    archivo_4 = open("palabras.txt","a")
    palabras_a_jugar(archivo_1,archivo_2,archivo_3,archivo_4)

main()