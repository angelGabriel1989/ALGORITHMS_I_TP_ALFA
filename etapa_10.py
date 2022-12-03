default = '999999'
def leer_linea_etapa10(archivo, default):
    linea = archivo.readlines()
    return linea.rstrip("\n").split(",")if linea else default

def generar_diccionario(lista):
    """
    Pasamos una línea convertida en lista (ejemplo : ej_linea_ar1)
    Genera un diccionario del estilo {palabra:cantidad}, donde cantidad son las veces que se repitió esa línea en el diccionario
    Me lo retona ya ordenado alfabeticamente de mayor a menor
    """
    diccionario = {}
    for palabra in lista:
        if palabra not in diccionario:
            diccionario[palabra]=1
        else:
            diccionario[palabra]+=1
    return sorted(diccionario,key = lambda item:item[0])

def filtrador_de_palabras_etapa_10_etapa10(archivo_texto,longitud):
    """
    Lee 1 archivo completo línea por línea.
    Cada línea lo convierte en una lista.
    Genera una nueva lista con todas las palabras_etapa_10 del archivo que contienen caracteres alfabéticos y que contengan la longitud que se recuperó del archivo configuracion.csv
    """
    archivo = open(archivo_texto)
    linea = leer_linea_etapa10(archivo_texto,default)
    lista_palabras_etapa_10 = []
    while linea:
        for posicion in linea:
            palabra = linea[posicion]
            if palabra.isalpha() and len(palabra) == longitud:
                lista_palabras_etapa_10.append(palabra.lower())
        linea = leer_linea_etapa10(archivo_texto)
    archivo.close()
    return lista_palabras_etapa_10
    
def eliminar_acentuados_etapa10(lista):
    #Filtrador_de_palabras_etapa_10_etapa10 me retorna una lista con palabras_etapa_10 todas en minúsculas, estén o no acentuadas
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


def palabras_etapa_10(archivo1, archivo2, archivo3):
    archivo_1 = open(archivo1,"r")
    archivo_2 = open(archivo2,"r")
    archivo_3 = open(archivo3,"r")
    archivo_4 = open("palabras_etapa_10.txt","a")
    configuracion = open("configuracion.csv")

    linea_config = leer_linea_etapa10("configuracion.csv")
    while linea_config[0] != "LONG_PALABRA_MIN":
        linea_config = leer_linea_etapa10("configuracion.csv")
    longitud = linea_config[1]
    configuracion.close()
    
    palabras_etapa_10_archivo1=[]
    palabras_etapa_10_archivo2=[]
    palabras_etapa_10_archivo3=[]

    diccionario_general = {}


    variable_control_archivo1 = True
    while variable_control_archivo1:
        palabras_etapa_10_arc1 = filtrador_de_palabras_etapa_10_etapa10(archivo1)
        palabras_etapa_10_sintilde1 = eliminar_acentuados_etapa10(palabras_etapa_10_arc1)
        #Agrego una lista de palabras_etapa_10 sin ningún caracter raro
        palabras_etapa_10_archivo1.append(palabras_etapa_10_sintilde1)
        #Generamos diccionario con la cantidad de veces que se repite la palabra en todo el Texto 1
        generar_diccionario(palabras_etapa_10_archivo1)
        variable_control_archivo1 = False
    
    variable_control_archivo2 = True
    while variable_control_archivo2:
        palabras_etapa_10_arc2 = filtrador_de_palabras_etapa_10_etapa10(archivo2)
        palabras_etapa_10_sintilde2 = eliminar_acentuados_etapa10(palabras_etapa_10_arc2)
        #Agrego una lista de palabras_etapa_10 sin ningún caracter raro
        palabras_etapa_10_archivo2.append(palabras_etapa_10_sintilde2)
        #Generamos diccionario con la cantidad de veces que se repite la palabra en todo el Texto 2
        generar_diccionario(palabras_etapa_10_archivo2)
        variable_control_archivo2 = False

    variable_control_archivo3 = True
    while variable_control_archivo3:
        palabras_etapa_10_arc3 = filtrador_de_palabras_etapa_10_etapa10(archivo3)
        palabras_etapa_10_sintilde3 = eliminar_acentuados_etapa10(palabras_etapa_10_arc3)
        #Agrego una lista de palabras_etapa_10 sin ningún caracter raro
        palabras_etapa_10_archivo3.append(palabras_etapa_10_sintilde3)
        #Generamos diccionario con la cantidad de veces que se repite la palabra en todo el Texto 3
        generar_diccionario(palabras_etapa_10_archivo3)
        variable_control_archivo3 = False
    
    #Armo el diccionario_general con todas las palabras_etapa_10 de los 3 archivos con la cantidad de veces que se repite
    
    for palabra in palabras_etapa_10_archivo1:
        if palabra not in diccionario_general:
            diccionario_general[palabra] = 1
        else:
            diccionario_general[palabra] +=1
    for palabra in palabras_etapa_10_archivo2:
        if palabra not in diccionario_general:
            diccionario_general[palabra] = 1
        else:
            diccionario_general[palabra] +=1
    for palabra in palabras_etapa_10_archivo3:
        if palabra not in diccionario_general:
            diccionario_general[palabra] = 1
        else:
            diccionario_general[palabra] +=1


    archivo_1.close()
    archivo_2.close()
    archivo_3.close()

    #Solo queda abierto archivo_4 -> "palabras_etapa_10.txt"

    # ---------------------- "APAREO" ----------------------------------- #
    long_archivo1 = len(palabras_etapa_10_archivo1)
    long_archivo2 = len(palabras_etapa_10_archivo2)
    long_archivo3 = len(palabras_etapa_10_archivo3)

    lista_variables_corte_control = [0,0,0] #-> [var_cor_arch1,var_cor_arch2,var_cor_arch3]
    while lista_variables_corte_control[0] <= long_archivo1 and lista_variables_corte_control[1]<= long_archivo2 and lista_variables_corte_control[2]<= long_archivo3:
        #Defino variables que van a almacenar las veces que se repiten las palabras_etapa_10 en cada archivo
        acumulador_pal_arc1 = 0
        acumulador_pal_arc2 = 0
        acumulador_pal_arc3 = 0
        minimo = min(palabras_etapa_10_archivo1[lista_variables_corte_control[0]][0],palabras_etapa_10_archivo2[lista_variables_corte_control[1]][0],palabras_etapa_10_archivo3[lista_variables_corte_control[2]][0])
        #Comienza a contar cuantas veces se repite la palabra en los 3 archivo
        while palabras_etapa_10_archivo1[lista_variables_corte_control[0]] == minimo and lista_variables_corte_control[0]==long_archivo1:
            acumulador_pal_arc1 = int(palabras_etapa_10_archivo1[lista_variables_corte_control[1]])
            lista_variables_corte_control[0] +=1
        while palabras_etapa_10_archivo2[lista_variables_corte_control[1]] == minimo and lista_variables_corte_control[1]==long_archivo1:
            acumulador_pal_arc1 = int(palabras_etapa_10_archivo2[lista_variables_corte_control[1]])
            lista_variables_corte_control[1] +=1
        while palabras_etapa_10_archivo1[lista_variables_corte_control[2]] == minimo and lista_variables_corte_control[2]==long_archivo1:
            acumulador_pal_arc1 = int(palabras_etapa_10_archivo3[lista_variables_corte_control[1]])
            lista_variables_corte_control[2] +=1
        #Una vez termine de contar cuantas veces se repite la palabra en cada archivo lo escribe en archivo_4
        archivo_4.append(str(minimo) + "," + str(acumulador_pal_arc1) + ","+ str(acumulador_pal_arc2) +  "," + str(acumulador_pal_arc3) + "\n")
    archivo_4.close()