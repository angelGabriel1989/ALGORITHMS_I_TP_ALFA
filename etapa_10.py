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
    return sorted(diccionario,key = lambda item:item[0])

def filtrador_de_palabras(archivo_texto,longitud):
    archivo = open(archivo_texto)
    linea = leer_linea(archivo_texto,default)
    lista_palabras = []
    while linea:
        for posicion in linea:
            palabra = linea[posicion]
            if palabra.isalpha() and len(palabra) == longitud:
                lista_palabras.append(palabra.lower())
        linea = leer_linea(archivo_texto)
    archivo.close()
    return lista_palabras
    
def eliminar_acentuados(lista):
    #Filtrador_de_palabras me retorna una lista con palabras todas en minúsculas, estén o no acentuadas
    vocales_minusculas = 'aeiou'
    lista_minusculas = []
    lista_aux = []

    for palabra in lista:
        if palabra.isupper():
            palabra = palabra.lower()
            lista_minusculas.append(palabra)
    
    for palabra in lista_minusculas:
        for caracter in palabra:
            if caracter in vocales_minusculas:
                if caracter == 'á' or caracter == 'ä' or caracter =='à':
                    caracter = 'a'
                elif caracter == 'é' or caracter == 'ë' or caracter =='è':
                    caracter = 'e'
                elif caracter == 'í' or caracter == 'ï' or caracter =='ì':
                    caracter = 'i'
                elif caracter == 'ó' or caracter == 'ö' or caracter =='ò':
                    caracter = 'o'
                elif caracter == 'ú' or caracter == 'ü' or caracter =='ù':
                    caracter = 'u'
        lista_aux.append(palabra)
    return lista_aux


def palabras(archivo1, archivo2, archivo3, archivo4,longitud):
    
    palabras_archivo1=[]
    palabras_archivo2=[]
    palabras_archivo3=[]

    diccionario_general = {}

    variable_control_archivo1 = True
    while variable_control_archivo1:
        palabras_arc1 = filtrador_de_palabras(archivo1, longitud)
        palabras_sintilde1 = eliminar_acentuados(palabras_arc1)
        #Agrego una lista de palabras sin ningún caracter raro
        palabras_archivo1.append(palabras_sintilde1)
        #Generamos diccionario con la cantidad de veces que se repite la palabra en todo el Texto 1
        generar_diccionario(palabras_archivo1)
        variable_control_archivo1 = False
    
    variable_control_archivo2 = True
    while variable_control_archivo2:
        palabras_arc2 = filtrador_de_palabras(archivo2,longitud)
        palabras_sintilde2 = eliminar_acentuados(palabras_arc2)
        #Agrego una lista de palabras sin ningún caracter raro
        palabras_archivo2.append(palabras_sintilde2)
        #Generamos diccionario con la cantidad de veces que se repite la palabra en todo el Texto 2
        generar_diccionario(palabras_archivo2)
        variable_control_archivo2 = False

    variable_control_archivo3 = True
    while variable_control_archivo3:
        palabras_arc3 = filtrador_de_palabras(archivo3, longitud)
        palabras_sintilde3 = eliminar_acentuados(palabras_arc3)
        #Agrego una lista de palabras sin ningún caracter raro
        palabras_archivo3.append(palabras_sintilde3)
        #Generamos diccionario con la cantidad de veces que se repite la palabra en todo el Texto 3
        generar_diccionario(palabras_archivo3)
        variable_control_archivo3 = False
    
    #Armo el diccionario_general con todas las palabras de los 3 archivos con la cantidad de veces que se repite
    
    for palabra in palabras_archivo1:
        if palabra not in diccionario_general:
            diccionario_general[palabra] = 1
        else:
            diccionario_general[palabra] +=1
    for palabra in palabras_archivo2:
        if palabra not in diccionario_general:
            diccionario_general[palabra] = 1
        else:
            diccionario_general[palabra] +=1
    for palabra in palabras_archivo3:
        if palabra not in diccionario_general:
            diccionario_general[palabra] = 1
        else:
            diccionario_general[palabra] +=1


    archivo1.close()
    archivo2.close()
    archivo3.close()

    #Solo queda abierto archivo_4 -> "palabras.txt"

    # ---------------------- "APAREO" ----------------------------------- #
    long_archivo1 = len(palabras_archivo1)-1
    long_archivo2 = len(palabras_archivo2)-1
    long_archivo3 = len(palabras_archivo3)-1

    lista_variables_corte_control = [0,0,0] #-> [var_cor_arch1,var_cor_arch2,var_cor_arch3]
    while lista_variables_corte_control[0] <= long_archivo1 and lista_variables_corte_control[1]<= long_archivo2 and lista_variables_corte_control[2]<= long_archivo3:
        #Defino variables que van a almacenar las veces que se repiten las palabras en cada archivo
        acumulador_pal_arc1 = 0
        acumulador_pal_arc2 = 0
        acumulador_pal_arc3 = 0
        minimo = min(palabras_archivo1[lista_variables_corte_control[0]][0],palabras_archivo2[lista_variables_corte_control[1]][0],palabras_archivo3[lista_variables_corte_control[2]][0])
        #Comienza a contar cuantas veces se repite la palabra en los 3 archivo
        while palabras_archivo1[lista_variables_corte_control[0]] == minimo and lista_variables_corte_control[0]==long_archivo1:
            acumulador_pal_arc1 = int(palabras_archivo1[lista_variables_corte_control[1]])
            lista_variables_corte_control[0] +=1
        while palabras_archivo2[lista_variables_corte_control[1]] == minimo and lista_variables_corte_control[1]==long_archivo1:
            acumulador_pal_arc1 = int(palabras_archivo2[lista_variables_corte_control[1]])
            lista_variables_corte_control[1] +=1
        while palabras_archivo1[lista_variables_corte_control[2]] == minimo and lista_variables_corte_control[2]==long_archivo1:
            acumulador_pal_arc1 = int(palabras_archivo3[lista_variables_corte_control[1]])
            lista_variables_corte_control[2] +=1
        #Una vez termine de contar cuantas veces se repite la palabra en cada archivo lo escribe en archivo_4
        archivo4.append(str(minimo) + "," + str(acumulador_pal_arc1) + ","+ str(acumulador_pal_arc2) +  "," + str(acumulador_pal_arc3) + "\n")
    archivo4.close()


    default = '999999'
    archivo_1 = open ("Cuentos.txt", "r")
    archivo_2 = open ("La araña negra - tomo 1.txt", "r")
    archivo_3 = open ("Las 1000 Noches y 1 Noche.txt", "r")
    archivo_4 = open("palabras.txt","a")
    configuracion = open("configuracion.csv")
    linea_config = leer_linea("configuracion.csv")
    while linea_config[0] != "LONG_PALABRA_MIN":
        linea_config = leer_linea("configuracion.csv")
    longitud = linea_config[1]
    configuracion.close()
    palabras(archivo_1,archivo_2,archivo_3,archivo_4, longitud)