from random import randint
import platform
import os
import time

def validez_longitud():
    """
    Función:
        validez_longitud
    Parámetros:
        longitud: longitud mínima de los caracteres que almacenamos en la lista de filtrador_palabra
    Salidas:
        longitud: longitud que usaremos para filtrar el diccionario con las posibles palabras
    Precondiciones:
    """
    longitud = input("Ingrese longitud de la palabra que desea adivinar: ")

    while longitud == str(0) or not longitud.isnumeric() and longitud != "":
        longitud = input("Error. Ingrese longitud de la palabra que desea adivinar: ")

    if longitud.isnumeric():
        if int(longitud) < 5:
            longitud = ""

    return longitud


### ------------------  SOLUCION DICCIONARIO ------------------- ###

texto_usar = """
    LAs az$ucena@s de blanco0_: raso e|rguíanse con cierto desmayo, com/o las
seño;.ritas en, en en en# t1ra2je@ de traje que que que que que la pobre había la..s camelias de color ca/rnoso hacían ,pensar.- en
tibias,,, desnudeces..., en grandes() señora|s indolentemente tendidas, mo0strando0 había Había
l[os misterio]s d°e s¨u piel de seda --_Borda, _Borda_ Bordeta_... nos asamos. ¡Por Dios! ¡Un traje de agua!
El valor del dólar blue tiene una diferencia sustancial con el dólar oficial, que se adquiere en los banco y que posee una cotización establecida. Su venta es en el mercado informal, sin regulaciones ni límites, y por eso se opera generalmente a un valor mayor que el dólar oficial.
"""
longitud_minima = 5


def obtener_texto(texto_usar):
    """Cesar Ortega"""
    # bucle que elimina caracteres que caracter.islpha not true
    aux = ""
    for letra in texto_usar:
        if letra.isalpha:
            aux += letra
        elif letra == " ":
            aux += letra

    texto_usar = aux    

    texto_usar =  texto_usar.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ñ","n").replace("ü","u").replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U").replace("Ñ","N").replace("Ü","U").casefold()
    lista_texto = texto_usar.split()
    return lista_texto

texto = obtener_texto(texto_usar) # CESAR ORTEGA

def eliminar_caracteres(lista_texto):
    """ Cesar Ortega
    Función:
        eliminar_caracteres
    Parámetros: 
        lista_texto: transforma todo el texto que se le pase a lista
    Salidas:
        lista_solo_alfabetica: almacenará cada palabra del texto sin caracteres especiales, solo letras
    Precondiciones:
        Las palabras deben estar contenida solo por caracteres alfabéticos
    """
    lista_solo_alfabetica=[]
    for palabra in lista_texto:
        for caracter in palabra:
            if not caracter.isalpha():
                palabra = palabra.replace(caracter,"")
        lista_solo_alfabetica.append(palabra)
    return lista_solo_alfabetica

lista_filtrada_solo_alfabeticos = eliminar_caracteres(texto)

def filtrador_palabra(lista):
    """
    Función:
        filtrador_palabra
    Parámetros:
        lista: Lista que almacena palabras solo con caracteres alfabéticos
    Salidas:
        lista_aux: Lista que almacenará caracteres de todo el texto 
    Precondiciones:
        Que la palabras no contengan caracteres especiales, de longitud mayor a 5 caracteres , que no se repitan y sean alfabeticos
    """
    lista_aux = []
    for palabra in lista:
        palabra=palabra.lower()
        if len(palabra) >= longitud_minima and not palabra in lista_aux:
            lista_aux.append(palabra)
    return lista_aux
"""print(filtrador_palabra(lista_filtrada_solo_alfabeticos))"""

lista_filtrada_mayores_5 = filtrador_palabra(lista_filtrada_solo_alfabeticos)

def diccionarValido():
    texto = obtener_texto(texto_usar)
    lista_filtrada = eliminar_caracteres(texto)
    lista_caracteres_mayor_5 = filtrador_palabra(lista_filtrada)

    return lista_caracteres_mayor_5

def eligePorCantidad(longitud_Caracteres, lista_diccionario):
    """
    Función:
        lista_candidatas
    Parámetros:
        diccionario: Usamos la clave del diccionario que creamos con la cant. veces que se repite la palabra
        longitud: Usamos de referencia para filtrar la lista con palabras que tengan esa longitud
    Salidas:
        lista_candidatas: Almacena las posibles palabras que vayan a entrar al juego
    Precondiciones:
    """
    lista_candidatas = []
    if int(longitud_Caracteres) >= longitud_minima:
        for i in range (len(lista_diccionario)):
            if len(lista_diccionario[i]) == longitud_Caracteres:
                lista_candidatas.append(lista_diccionario[i])
    else:
        for i in range(len(lista_diccionario)):
            lista_candidatas.append(lista_diccionario[i])
    return lista_candidatas

def randomPalabraElegida(lista_candidatas):
    """
    Función:
        palabra_aleatoria
    Parámetros:
        lista_candidatas: Almacena las posibles palabras que vayan a entrar al juego
    Salidas:
        palabraSeleccionada: Elige una palabra al azar haciendo uso de la librería random
    Precondiciones:
    """
    from random import randint
    numeroMagico = int(randint(0,len(lista_candidatas)-1))
    palabraElegida = lista_candidatas[numeroMagico]
    return palabraElegida

def diccionario_palabras_repetidas(texto):
    """
    Función:
        diccionario_palabras_repetidas
    Parámetros:
        texto: usamos todo el texto sin caracteres especiales, para comprobar cuantas veces se repite la clave en ese texto
    Salidas:
        diccionario_palabra: diccionario que almacena como clave la palabra sin repetir y como valor las veces que se repite en todo el texto
    Precondiciones:
    """
    diccionario_palabra = {}
    contador_palabra = 0
    for palabra_filtrador in lista_filtrada_mayores_5:
        contador_palabra = texto.count(palabra_filtrador)
        diccionario_palabra[palabra_filtrador]=contador_palabra
    return dict(sorted(diccionario_palabra.items(), key = lambda diccionario:diccionario[0]))

"""print(diccionario_palabras_repetidas(lista_filtrada_solo_alfabeticos))"""


##########----------------------------------------------- FIN TEMA DICCIONARIO ----------------------------------------------------- ##########

######### ----------------------------------------------- VALIDACION DE CARACTERES --------------------------------------------------##########


def aplanarLetra():
    """ Gabriel Barros
    funcion que aplana el texto """
    letra = input("Ingrese una letra (0 o esc salir): ")
    diccionario =  [("áÁàÀ","a"), ("éÉëËèÈ", "e"), ("íÍìÌ", "i"),("óÓÖöòÒ", "o"),("úÚüÜùÙ", "u") ]

    for item in diccionario:
        if letra in item[0]:
            letra = item[1]
    
    letra = letra.lower()

    return letra

def ingresoLetra(letrasBuenas, letrasMalas):
    """
    Función:
        ingresoLetra
    Parámetros:
        letrasBuenas: Acumulador de letras que coinciden con la palabra a adivinar
        letraMalas: Acumulador de letras que no coinciden con la palabra a adivinar
    Salidas:
        letra: Se retorna una letra que no pertenece 
    Precondiciones:
        Hay que ingresar una letra
    """

    letra = aplanarLetra()
    
    letra = letra.lower() # desestimando mayusculas o minusculas

    while letra in letrasBuenas or letra in letrasMalas:
        print("letra repetida")
        letra = aplanarLetra()
    return letra

def funcionEscape(letra):
    """
    Función:
        funcionEscape
    Parámetros:
        letra: letra que ingresó el usuario
    Salidas:
        intentoEscape: True si letra es "esc" o "0", False si letra no es "esc" o "0"
    """
    """ Evalua si escapas """
    return letra == "esc" or letra == "0"
    
def correccionLetraMala(letra, letrasBuenas, letrasMalas):
    """
    Función:
        correccionLetraMala
    Parámetros:
        * letra: Letra que ingresó el usuario
        * letrasBuenas: Almacena caracteres que están en la palabra a adivinar
        * letrasMalas: Almacena caracteres que NO están en la palabra a adivinar
    Salidas:
        * salida: Lista que contiene letra ingresada por el usuario y un Booleano
    Precondiciones:
        * Letra debe tener longitud mayor a 1
    Postcondiciones:
        * Devuelve un lista con la letra válida y un booleano para evaluar si continúas o no jugando
    """
    cant_control = 10
    variable_de_control = 0
    evaluacionLetra = None
    salida = []
    while variable_de_control < cant_control:
        print("Ingreso erroneo")
        letra = ingresoLetra(letrasBuenas, letrasMalas)
        intentoEscapar = funcionEscape(letra)
        if intentoEscapar:
            evaluacionLetra = False
            variable_de_control = cant_control
        else:
            letraValida = esSoloUnaLetra(letra)
            if letraValida:
                evaluacionLetra = True
                variable_de_control = cant_control
            else:
                pass
    salida.append(letra)
    salida.append(evaluacionLetra)          
    return salida       

def esSoloUnaLetra(letra):
    """
    Función:
        esSoloUnaLetra
    Parámetros:
        letra: Letra que ingresó el usuario
    Salidas:
        esLetra: Booleano - > Variable de control
    Precondiciones:
        La letra debe tener longitud 1 y ser alfabético
    """
    longitud_requerida = 1
    return len(letra) == longitud_requerida and letra.isalpha()

def letraValida(letrasBuenas, letrasMalas):
    """
    Función:
        letraValida
    Parámetros:
        * letrasBuenas: Almacena caracteres que están en la palabra a adivinar
        * letrasMalas: Almacena caracteres que NO están en la palabra a adivinar
    Salidas:
        * salidaLetra: Retorna una lista con una variable booleano y la letra ingresada
    Precondiciones:
        * Letra de longitud 1
        * Alfabetica
        * No se repita la letra
        * Evalua si continúas jugando o no
    """
    salidaLetra = []
    continuaJugando = None
    variable_de_control = 0
    while variable_de_control < 1:
        letra = ingresoLetra(letrasBuenas, letrasMalas)
        intentoEscape = funcionEscape(letra) 
        if intentoEscape:
            continuaJugando = False
            variable_de_control = 10
        else:
            caracterValido = esSoloUnaLetra(letra)
            if caracterValido:
                continuaJugando = True
                variable_de_control = 10
            else:
                devolucionDeCorrecion = correccionLetraMala(letra,letrasBuenas, letrasMalas)
                # print(f"acá hay que almacenar está variable en letras {devolucionDeCorrecion[0]}")
                if devolucionDeCorrecion[1]:
                    continuaJugando = True
                    letra = devolucionDeCorrecion[0]          
                    variable_de_control = 10
                else:
                    continuaJugando = False
                    letra = devolucionDeCorrecion[0]
                    variable_de_control = 10
    salidaLetra.append(letra)
    salidaLetra.append(continuaJugando)
    # print("salida buena está saliendo {}".format(salidaLetra))
    return salidaLetra

def letraBuena(letra, palabraElegida):
    """
    Función:
        letraBuena
    Parámetros:
        letra: Letra que ingresó el usuario
        palabraElegida: Palabra aleatoria que eligió el sistema
    Salidas:
        esBuena: Booleano -> Variable de Control
    Precondiciones:
        Que letra ingresada esté en la palabra elegida
    """
    return letra in palabraElegida

def muestraAciertosErrores(letra, muestraParcial, contadorAciertos, contadorErrores, palabraAhorcado):
    """
    Función:
        muestraAciertosErrores
    Parámetros:
        letra, muestraParcial, contadorAciertos, contadorErrores, palabraAhorcado
    Salidas:
        Imprime el tablero
    """
    if letra in palabraAhorcado:
        print(f"Muy bien jajaja {muestraParcial} Aciertos: {contadorAciertos} Desaciertos: {contadorErrores} ")
    else:
        print(f"Lo siento {muestraParcial} Aciertos: {contadorAciertos} Desaciertos: {contadorErrores} ")
    
    return None

def acumularLetras(letra, letras):
    """
    Función:
        acumularLetras
    Parámetros:
        letra: Letra que ingresó el usuario
        letras: Variable que almacena TODOS LOS CARACTERES, estén o no estén en la palabra a adivinar
    Salidas:
        Letras acumuladas
    """
    letras += letra
    return letras



############## -------------------------------------- EVOLUCION DE LA INTERFAZ ------------------------------------ ######################
def muestraPalabraEncriptada(letras, palabraAhorcado):
    """
    Función:
        muestraPalabraEncriptada
    Parámetros:
        letras: Variable que almacenó TODOS LOS CARACTERES, estén o no estén en la palabra a adivinar
        palabraAhorcado: palabra aleatoria elegida por el sistema
    Salidas:
        Encripta la palabra 
    """
    muestraParcial = ""
    for i in range (len(palabraAhorcado)):
        if palabraAhorcado[i] in letras:
            muestraParcial += palabraAhorcado[i]
        else:
            muestraParcial += "?"
    
    return muestraParcial

def printeoAciertoError(letra, muestraParcial, contadorAciertos, contadorErrores, palabraAhorcado, letrasMalas):
    """
    Función: 
        printeoAciertoError
    Parámetros:
        letra: 
        muestraParcial: palabra a adivinar en formato "?"
        contadorAciertos: cantidad de aciertos de la partida
        contadorErrores: cantidad de desaciertos de la partida
        palabraAhorcado: palabra aleatoria elegida por el sistema
        letrasMalas: variable que almacena todos los caracteres erróneos
    Salidas:
        Imprime el tablero
    """
    if letra in palabraAhorcado:
        print(f"\nMuy bien jajaja {muestraParcial} Aciertos: {contadorAciertos} Desaciertos: {contadorErrores} - {letrasMalas}\n")
    else:
        print(f"Lo siento {muestraParcial} Aciertos: {contadorAciertos} Desaciertos: {contadorErrores} - {letrasMalas}\n ")
    
    return None

def ganaPierdo(muestraParcial, palabraAhorcado, contadorErrores,puntaje):
    """
    Función: 
        ganaPierdo
    Parámetros:
        muestraParcial: transforma palabra a adivinar en "?"
        palabraAhorcado: palabra aleatoria elegida por el sistema
        contadorErrores
        puntaje: puntaje total por partida
    Salidas:
        Imprime si ganó o perdió el usuario
    """
    if muestraParcial == palabraAhorcado:
        contadorErrores = 9
        print(f"\nHAS GANADO! SU PUNTAJE ES: {puntaje}\n")
        # nueva_partida(puntaje)
    elif contadorErrores == 8:
        print(f"\nPERDISTE! SU PUNTAJE ES: {puntaje}\nPalabra a adivinar era: {palabraAhorcado}\n")
        # nueva_partida(puntaje)
    else:
        pass
    return contadorErrores

def Asignacion_Puntajes(tot_ganados,tot_perdidos):
    """
    Función: 
        Asignacion_Puntajes
    Parámetros:
        tot_ganados: Acumula la cantidad de puntos por cada acierto
        tot_perdidos: Acumula la cantidad de puntos por cada desacierto
    Salidas:
        Retorna el puntaje total
    """
    tot_ganados = int(tot_ganados)
    tot_perdidos = int(tot_perdidos)
    return tot_ganados - tot_perdidos


############# --------------------------------------------------------- PARTIDA DE JUEGO ------------------------------- #############################
def nueva_partida():
    """
    Función: nueva_partida
    Parámetros:
        puntaje_anterior: Almacena el puntaje acumulador de todas las partidas jugadas
    Salidas:
        tot: Acumula el puntaje de todas las partidas jugadas
    """
    consulta_nueva_partida = ""

    total = jugar()

    variable_de_control = 1
    while variable_de_control != 0:
        consulta_nueva_partida = input("Desea jugar una nueva partida? (s/n): ")

        if consulta_nueva_partida == "s": 
            puntaje_nuevo = jugar()
            total += puntaje_nuevo
            print(f"\nEL TOTAL DE LAS PARTIDAS JUGADAS {total}\n")
        else:    
            print(f"\nEL TOTAL DE LAS PARTIDAS JUGADAS {total}")
            variable_de_control = 0
    
    return None


def jugar():
    errores = aciertos = contador = total_puntajes_ganados = total_puntajes_perdidos = 0
    # aciertos = 0
    # contador = 0
    # total_puntajes_ganados = 0
    # total_puntajes_perdidos = 0
    letrasMalas = letrasBuenas = ""
    # letrasBuenas = ""
    cant_intentos = 7
    puntos_por_acierto = 10
    puntos_por_desaciertos = -5
    longitud = int(validez_longitud())
    lista_diccionario = diccionarValido()
    lista_Igualdad_Caracteres = eligePorCantidad(longitud, lista_diccionario)
    palabraElegida = randomPalabraElegida(lista_Igualdad_Caracteres)
    puntaje = Asignacion_Puntajes( total_puntajes_ganados, total_puntajes_perdidos)
    muestraParcial = muestraPalabraEncriptada(letrasBuenas, palabraElegida)

    print(f"Palabra a adivinar: {muestraParcial}  Aciertos: {aciertos}  Desaciertos: {errores}")
    while contador <= cant_intentos:

        salidaLetra = letraValida(letrasBuenas, letrasBuenas)
        sigueJugando = salidaLetra[1]
        letra = salidaLetra[0] 

        if sigueJugando:

            esBuena = letraBuena(letra, palabraElegida)

            if esBuena:
                aciertos += 1
                total_puntajes_ganados = aciertos * puntos_por_acierto
                puntaje = Asignacion_Puntajes( total_puntajes_ganados, total_puntajes_perdidos)
                letrasBuenas = acumularLetras(letra, letrasBuenas)
                muestraParcial = muestraPalabraEncriptada(letrasBuenas, palabraElegida)
                printeoAciertoError(letra, muestraParcial, aciertos, errores, palabraElegida, letrasMalas)
                contador = ganaPierdo(muestraParcial, palabraElegida, errores,puntaje)
                    
            elif letra not in letrasMalas: 
                errores += 1
                total_puntajes_perdidos = errores * puntos_por_desaciertos
                puntaje = Asignacion_Puntajes( total_puntajes_ganados, total_puntajes_perdidos)
                contador += 1
                letrasMalas = acumularLetras(letra, letrasMalas)
                muestraParcial = muestraPalabraEncriptada(letrasBuenas, palabraElegida)
                printeoAciertoError(letra, muestraParcial, aciertos, errores, palabraElegida, letrasMalas)
                contador = ganaPierdo(muestraParcial, palabraElegida, errores,puntaje)
            else:
                print("LETRA REPETIDA")
        else:
            contador = 10
            print("\nJUEGO FINALIZADO\n")


    return puntaje


###########---------------------------------------------------- ETAPA SIETE NOELIA SALVATIERRA------------------------------------------------- ###############

import csv
from tkinter import *
from tkinter import messagebox


def crear_ventana_de_inicio():
    #Esta funcion crea la ventana principal(la gris oscura)
    global ventana_principal
    ventana_principal=Tk()
    ventana_principal.title("Login Alfajor")
    ventana_principal.resizable(0,0)
    ventana_principal.geometry("280x180")
    # ventana_principal.iconbitmap("Ahorcado 1.ico")
    ventana_principal.config(background="gray")
    global usuario
    global clave
    usuario = StringVar()
    clave = StringVar()
    global entrada_usuario
    global entrada_clave
    #Label "Comentario de Bienvenida"
    comentario1 = Label(text = "Bienvenido al juego del Ahorcado")
    comentario1.pack()
    comentario1.place(x=30, y=20)
    comentario1.config(background="LightGreen")
    #Label "Usuario"
    usuario_a_ingresar= Label(text = "Usuario Jugador: ")
    usuario_a_ingresar.pack()
    usuario_a_ingresar.place(x=10, y=70)
    #Label "Clave"
    clave_a_ingresar= Label(text = "Clave: ")
    clave_a_ingresar.pack()
    clave_a_ingresar.place(x=10,y=100)
    #Caja de texto para Usuario
    entrada_usuario = Entry(ventana_principal,textvariable=usuario)
    entrada_usuario.pack()
    entrada_usuario.place( x=120, y=70)
    #Caja de texto para Clave
    entrada_clave = Entry(ventana_principal,textvariable=clave)
    entrada_clave.place( x=120, y=100)
    entrada_clave.config(show="*")
    #Boton Ingresar
    boton_ingresar = Button(ventana_principal,text="Ingresar",command = validar_usuario_nombre_y_clave_registrado)
    boton_ingresar.pack()
    boton_ingresar.place(x=30,y=140)
    #Boton Iniciar partida
    boton_iniciar_partida = Button(ventana_principal,text="Iniciar partida",command=destruir_ventana_principal)
    boton_iniciar_partida.pack()
    boton_iniciar_partida.place(x=90,y=140)
    #Boton Registrarse
    boton_registrarse = Button(ventana_principal,text="Registrarse",command = registrar_jugador)
    boton_registrarse.pack()
    boton_registrarse.place(x=180,y=140)

    ventana_principal.mainloop()

    

def registrar_jugador():
    #Esta funcion crea la ventana registro de jugador
    global ventana_registro
    ventana_registro = Toplevel(ventana_principal)
    ventana_registro.title("Registro")
    ventana_registro.geometry("300x280")
    # ventana_registro.iconbitmap("Ahorcado 1.ico")
    global nombre_usuario_new
    global clave_new
    global clave_new_bis
    nombre_usuario_new= StringVar() 
    clave_new= StringVar() 
    clave_new_bis=StringVar()
    global entrada_nombre_usuario_nuevo
    global entrada_clave_nueva
    global entrada_clave_nueva_otra_vez
    #Label "Usuario_nuevo"
    etiqueta_usuario_nuevo = Label(ventana_registro,text = "Ingrese nombre: ")
    etiqueta_usuario_nuevo.pack()
    etiqueta_usuario_nuevo.place(x=10, y=20)
    #Label "Clave_nueva"
    clave_nueva = Label(ventana_registro,text = "Ingrese una Clave: ")
    clave_nueva.pack()
    clave_nueva.place(x=10,y=100)
    #Label "Pedido clave nueva otra vez"
    clave_nueva_otra_vez= Label(ventana_registro,text = "Ingresela otra vez: ")
    clave_nueva_otra_vez.pack()
    clave_nueva_otra_vez.place(x=10,y=180)
    #Caja de texto para Usuario-nuevo
    entrada_nombre_usuario_nuevo = Entry(ventana_registro,textvariable=nombre_usuario_new)
    entrada_nombre_usuario_nuevo.pack()
    entrada_nombre_usuario_nuevo.place( x=120, y=20)
    #Boton en caja de texto para nombre de usuario nuevo
    boton_entrada_usuario_nuevo = Button(ventana_registro,text="Hecho",command=validar_entrada_nombre_usuario_nuevo)
    boton_entrada_usuario_nuevo.pack()
    boton_entrada_usuario_nuevo.place(x=150,y=50)
    #Caja de texto para Clave_nueva
    entrada_clave_nueva = Entry(ventana_registro,textvariable=clave_new)
    entrada_clave_nueva.pack()
    entrada_clave_nueva.place( x=120, y=100)
    entrada_clave_nueva.config(show="*")
    #Boton en caja de texto para clave de usuario nuevo
    boton_entrada_clave_nueva = Button(ventana_registro,text="Hecho",command=validar_entrada_clave_nueva)
    boton_entrada_clave_nueva.pack()
    boton_entrada_clave_nueva.place(x=150,y=130)
    #Caja de texto para Clave_nueva otra vez
    entrada_clave_nueva_otra_vez= Entry(ventana_registro,textvariable=clave_new_bis)
    entrada_clave_nueva_otra_vez.pack()
    entrada_clave_nueva_otra_vez.place( x=120, y=180)
    entrada_clave_nueva_otra_vez.config(show="*")
    #Boton en caja de texto para clave  ingresada otra vez de usuario nuevo
    boton_entrada_clave_nueva = Button(ventana_registro,text="Hecho",command=validar_entradas_claves_nuevas)
    boton_entrada_clave_nueva.pack()
    boton_entrada_clave_nueva.place(x=150,y=200)
    #Boton Crear Usuario Nuevo Completo
    boton_usuario_nuevo= Button(ventana_registro,text="Registrarse",command = lambda:registrar_usuarios_nuevos(nombre_usuario_new.get(), clave_new.get()))
    boton_usuario_nuevo.pack()
    boton_usuario_nuevo.place(x=100,y=250)



def validar_nombre_jugador_nuevo():
    #Esta funcion valida el nombre del usuario nuevo que quiere registrase(si tiene entre 4 o 15 caracteres,si tiene guion,letra y nuemro)
    info_nombre_usuario_nuevo=nombre_usuario_new.get()
    posicion=0
    longitud_minima=4
    longitud_maxima=15
    guion=False
    letra=False
    numero=False
    simbolo_invalido=False
    if longitud_minima <= len(info_nombre_usuario_nuevo) <= longitud_maxima:
        while(posicion < len(info_nombre_usuario_nuevo) and not simbolo_invalido):
            if (info_nombre_usuario_nuevo[posicion] == "_"):
                guion=True
            elif (info_nombre_usuario_nuevo[posicion].isalpha()):
                letra=True
            elif (info_nombre_usuario_nuevo[posicion].isnumeric()):
                numero=True
            else:
                simbolo_invalido=True
            posicion = posicion + 1
    return guion and letra and numero and not simbolo_invalido
    


def validar_clave_de_jugador_nuevo():
    #Esta funcion valida la clave nueva del usuario nuevo(si tiene mayus,munus,numero,simbolo valido y no simbolos invalidos)
    info_clave_usuario_nuevo=str(clave_new.get())
    hay_mayuscula = False
    hay_minuscula = False
    tiene_digito = False
    tiene_simbolo_valido = False
    tiene_simbolo_invalido = False
    long_minima = 8
    long_maxima = 12
    posicion = 0
    if long_minima <= len(info_clave_usuario_nuevo) <= long_maxima:
         while (posicion < len(info_clave_usuario_nuevo) and (not info_clave_usuario_nuevo[posicion] in ['Á','É','Í','Ó','Ú','á','é','í','ó','ú']) and not tiene_simbolo_invalido):
            if info_clave_usuario_nuevo[posicion].isupper():
                hay_mayuscula = True
            elif info_clave_usuario_nuevo[posicion].islower():
                hay_minuscula = True
            elif info_clave_usuario_nuevo[posicion].isdigit():
                tiene_digito = True
            elif info_clave_usuario_nuevo[posicion] in ['-','_']:
                tiene_simbolo_valido = True
            else:
                tiene_simbolo_invalido = True
            posicion = posicion + 1
    return hay_mayuscula and hay_minuscula and tiene_digito and tiene_simbolo_valido and not tiene_simbolo_invalido



def validar_entrada_nombre_usuario_nuevo():
    #Esta funcion valida si el nombre del usuario esta ya registrado (leyendo el archivo registracion), si no es blanco anteriormente y manda mensajes
    info_nombre_usuario_nuevo=nombre_usuario_new.get()
    usuario_a_registrar=False
    linea=" "
    validacion_entrada_nombre_usuario_nuevo=validar_nombre_jugador_nuevo()
    if info_nombre_usuario_nuevo != "":
        archivo=open("00- registros.csv", "r")
        linea=archivo.readline()
        while linea != "" and (not usuario_a_registrar):
            linea=archivo.readline()
            linea_convertida_a_lista= linea.rstrip("\n").split(",")
            print(linea_convertida_a_lista[0] ,info_nombre_usuario_nuevo )
            if linea_convertida_a_lista[0] == info_nombre_usuario_nuevo:
                usuario_a_registrar=True
                messagebox.showerror(message="Nombre de Usuario no valido. Ya existe.")
                entrada_nombre_usuario_nuevo.delete(0,END)
        if not validacion_entrada_nombre_usuario_nuevo:
            messagebox.showerror(message="El usuario no existe pero es invalido (tiene que tener una letra,un numero y un guion")
            entrada_nombre_usuario_nuevo.delete(0,END)
        else:
            messagebox.showinfo(message="El nombre no exiSte y es valido.Ingrese la clave")
        archivo.close()
    else:
        messagebox.showerror(message="El nombre no puede estar en blanco")
        
            
        
def validar_entrada_clave_nueva():
    #Esta funcion valida si la clave ingresada por el usuario a registrar es valida y sino salen ventanas emergentes
    validacion_entrada_clave_usuario_nuevo_valido=validar_clave_de_jugador_nuevo()
    info_clave_usuario_nuevo=str(clave_new.get())
    if info_clave_usuario_nuevo != " ":
        if not validacion_entrada_clave_usuario_nuevo_valido:
            messagebox.showerror(message="Clave invalida")
            entrada_clave_nueva.delete(0,END)
        else:
            messagebox.showinfo(message="clave valida,Continue") 
    else:
        messagebox.showerror(message="La clave no puede estar en blanco")
           


def validar_usuario_nombre_y_clave_registrado():
    #Esta funcion valida en la ventana principal si el usuario pone el nombre y clave correctos(si ya esta registardo),abriendo el archivo registracion.csv y leyendolo
    nombre_usuario_registrado=usuario.get()
    clave_usuario_registrado=str(clave.get())
    usuario_registrado=False
    clave_registrada=False
    linea=" "
    if nombre_usuario_registrado != "" and clave_usuario_registrado != "":
        archivo=open("00- registros.csv", "r")
        while linea != "" and (not usuario_registrado):
            linea=archivo.readline()
            if linea != "":
                usuario_linea, clave_linea = linea.rstrip("\n").split(",")
                usuario_registrado=False
                clave_registrada=False
                if usuario_linea == nombre_usuario_registrado:
                    usuario_registrado=True
                    if clave_linea == clave_usuario_registrado:
                        clave_registrada=True
            else:
                linea=""
        archivo.close()
        if usuario_registrado and clave_registrada:
            ingresar_usuarios_a_la_sala_de_juego(nombre_usuario_registrado)
            messagebox.showinfo(message="Usuario y clave correctos.Si quiere jugar presione <INICIAR PARTIDA>")
            entrada_usuario.delete(0,END)
            entrada_clave.delete(0,END)
        elif not usuario_registrado:
            messagebox.showerror(message="El Usuario no existe. Ingrese el nombre correcto o Regístrese.")
        elif not clave_registrada:
            messagebox.showerror(message="La clave es incorrecta. Ingrese el Usuario y la Clave nuevamente.")
    else:
        messagebox.showerror(message="Nombre de Usuario y/o Clave no validos. No pueden estar en blanco.")
    entrada_usuario.delete(0,END)
    entrada_clave.delete(0,END)



def ingresar_usuarios_a_la_sala_de_juego(nombre_jugador):
    #Esta funcion (cuando todo esta bien validado) guarda el nombre del usuario en un archivo csv y a mediada que ingresan mas jugadores se sigue guardando
    lista_jugador=[nombre_jugador]
    with open("00- ingresos.csv","a",newline="") as file:
        writer=csv.writer(file,delimiter=",")
        writer.writerow(lista_jugador)
    contador_jugadores=0
    with open("00- ingresos.csv", "r",newline="") as file:
        linea = file.readline()
        while linea != "":
            contador_jugadores=contador_jugadores+ 1
            linea = file.readline()
            if contador_jugadores == 4:
                messagebox.showinfo(message="Recuerde que solo se permite el ingreso de hasta 4 jugadores\nA continuacion se bloquearan las cajas de texto")
                entrada_usuario["state"] = "disabled"
                entrada_clave["state"] = "disabled"


def contar_jugadores():
    #Cuenta la cantidad de jugadores que ingresaron a la sala de juego una vez que se presiono el boton iniciar partida
    contador_jugadores=0
    with open("00- ingresos.csv", "r",newline="") as file:
        linea = file.readline()
        while linea != "":
            contador_jugadores=contador_jugadores+ 1
            linea = file.readline()
    return(contador_jugadores)


def destruir_ventana_principal():
    ventana_principal.destroy()
    


def asignar_turnos_a_todos_los_jugadores():
    #Devuelve un diccionario con clave el nombre de los jugadores y el valor es el turno aleatorio y unico que lo toco a cada uno una vez que se toque el boton iniciar partida
    cantidad_jugadores=contar_jugadores()
    lista_de_turnos=range(1,cantidad_jugadores + 1)
    lista_para_obtener_nombres_de_jugadores=[]
    diccionario_jugadores_con_turnos_y_palabras_magicas_asignadas={}
    import random 
    lista_aleatorios_unicos=random.sample(lista_de_turnos,len(lista_de_turnos))
    with open("00- ingresos.csv", "r",newline="") as file:
        linea = file.readline()
        while linea != "":
            nombre_jugador_1=str(linea.rstrip())
            lista_para_obtener_nombres_de_jugadores.append(nombre_jugador_1)
            linea = file.readline()
    diccionario_jugadores_con_turnos_y_palabras_magicas_asignadas=dict(zip(lista_para_obtener_nombres_de_jugadores, lista_aleatorios_unicos))
    for clave in diccionario_jugadores_con_turnos_y_palabras_magicas_asignadas:
        print(f"El jugador {clave} tiene turno numero {diccionario_jugadores_con_turnos_y_palabras_magicas_asignadas[clave]}")
    print("A jugar!")

    # limpiar_pantalla()

    return diccionario_jugadores_con_turnos_y_palabras_magicas_asignadas
    #Aca se importaria lo de la parte uno e inmediatamente abajo de esto llamamos a la funcion jugar


    

def asignar_turnos_a_todos_los_jugadores_menos_ganador(ganador):
    #Tomo a ganador como string (hacer la conversion)
    #Funcion que recibe el nombre de ganador,lee el archivo ingresos.csv y devuelve la asignacion de todos los turnos menos el del ganador que sera el primero en empezar la n partida
    #En este caso si se quiere jugar otro partida se lee otra vez el archivo ingresos,jugando los mismos jugadores
    diccionario_jugadores_con_turnos={}
    cantidad_jugadores=contar_jugadores()
    primer_turno_para_el_ganador=1
    lista_no_ganadores=[]
    lista_ganador=[str(ganador)]
    archivo=open("00- ingresos.csv", "r")
    jugador=leer_linea(archivo)
    while jugador != [" "]:
        if lista_ganador == jugador:
            lista_ganador.append(primer_turno_para_el_ganador)
        else:
            lista_no_ganadores.append(jugador[0])
        jugador=leer_linea(archivo)
    archivo.close()
    lista_de_turnos_no_ganadores=range(2,cantidad_jugadores + 1)
    import random 
    lista_aleatorios_unicos_no_ganadores=random.sample(lista_de_turnos_no_ganadores,len(lista_de_turnos_no_ganadores))
    diccionario_jugadores_con_turnos=dict(zip(lista_no_ganadores, lista_aleatorios_unicos_no_ganadores))
    #Agrego el ganador con su turno
    if not lista_ganador[0] in diccionario_jugadores_con_turnos:
        diccionario_jugadores_con_turnos[lista_ganador[0]]=lista_ganador[1]
    for clave in diccionario_jugadores_con_turnos:
        print(f"El jugador {clave} tiene turno numero {diccionario_jugadores_con_turnos[clave]}")
    print("A jugar!")
    return diccionario_jugadores_con_turnos


def leer_linea(archivo_a_estudiar):
    linea=archivo_a_estudiar.readline()
    if linea != "":
        devolver=linea.rstrip().split(",")
    else:
        devolver=[" "]
    return devolver
    
                
def limpiar_pantalla():
    time.sleep(0.5)

    if platform.system() == 'windows':
        os.system('cls')
    else:
        os.system('clear')
    return None    


def validar_entradas_claves_nuevas():
    #Esta funcion valida en la venta de registro de jugador si la clave ingresada(validada anteriormente) y la misma clave ingresada otra vez es igual 
    info_clave_usuario_nuevo=str(clave_new.get())
    info_clave_usuario_nuevo_bis=str(clave_new_bis.get())
    if info_clave_usuario_nuevo != info_clave_usuario_nuevo_bis:
        messagebox.showerror(message="Las claves ingresadas no coinciden")
        entrada_clave_nueva_otra_vez.delete(0,END)
    else:
        messagebox.showinfo(message="Las claves coinciden,continue")


def registrar_usuarios_nuevos(datos_nombre_usuario_nuevo,datos_clave_usuario_nuevo):
    #Esta funcion (cuando todo esta bien validado) guarda los datos del usuario nuevo en un archivo llamado registracion.csv e imprime arriba "registro completado con exito"
    datos_usuario_nuevo=[datos_nombre_usuario_nuevo,datos_clave_usuario_nuevo]
    with open("registracion.csv","a",newline="") as file:
        writer=csv.writer(file,delimiter=",")
        writer.writerow(datos_usuario_nuevo)
    messagebox.showinfo(message="Registro completado con exito")
    entrada_nombre_usuario_nuevo.delete(0,END)
    entrada_clave_nueva.delete(0,END)
    entrada_clave_nueva_otra_vez.delete(0,END)




###########----------------------------------------------------- ETAPA OCHO LAUTARO LAFFONT ------------------------------------------------- ###############


# RETORNA DOS VALORES: CANTIDAD DEJUGADORES Y LISTA DE USUARIOS 

def jugadores_lautaro():   
    
    jugadores = int(randint(1,4))
    palabra = "jugador"
    lista_devolver = []

    for i in range (jugadores):
        lista_devolver.append(str(palabra+str(i)))


    return lista_devolver

def quienJuegaPrimero(lista):
    cantidad_jugadores = 4
    
    jugador_posicion = {"Jugador_1" : 2, "Jugador_2": 1, "Jugador_3" : 4, "Jugador4" : 3}


    return jugador_posicion
        



###########---------------------------------------------- NUEVA PARTE DEL CODIGO ----------------------------------------------- #############
###########------------------------------------------- HAY QUE DESARROLLAR INTERFAZ -------------------------------------------- #############
###########------------------------------------------- FUNCIONES DE ETAPA 8 Y 9 ------------------------------------------------ #############

def elegir_palabra(longitud):
    "Gabriel Barros"
    lista_diccionario = diccionarValido()
    lista_Igualdad_Caracteres = eligePorCantidad(longitud, lista_diccionario)
    palabraElegida = randomPalabraElegida(lista_Igualdad_Caracteres)
    return palabraElegida

def consolidar_posiciones_y_palabras(jugadores, longitud):
    """
    Función que toma los jugadores y las posiciones y les carga las palabras sin repetir
    Hecha por G.B
    """
    import random
    dicc_valido = diccionarValido() # esta función es la que me retorna palabras candidatas

    numero_jugadores = int(len(jugadores))

    # RECORRIENDO DICCIONARIO Y RECORTANDO PALABRAS CANDIDATAS PARA JUGAR
    i = 0
    dicc_truncado = []
    while i < len(dicc_valido):
        # print(f"{dicc_valido[i]}, tipo: {type(dicc_valido[i])}")
        if int(len(dicc_valido[i])) == int(longitud):
            dicc_truncado.append(dicc_valido[i])
            i += 1
        else:
            i += 1
  
    palabras_elegidas = random.sample(dicc_truncado, numero_jugadores)

    devolver = {}
    acceso = 0
    for i in sorted(jugadores, key = lambda i : jugadores[i]):
        clave = i
        devolver[clave] = (jugadores[i], palabras_elegidas[acceso])

        acceso += 1

    return devolver

####################### ------------------------------------------COMENZANDO ETAPA 9-------------------------------------- ##################################

####################### ------------------------------------------COMENZANDO ETAPA 9-------------------------------------- ##################################

####################### ------------------------------------------COMENZANDO ETAPA 9-------------------------------------- ##################################

####################### ------------------------------------------COMENZANDO ETAPA 9-------------------------------------- ##################################

####################### ------------------------------------------COMENZANDO ETAPA 9-------------------------------------- ##################################

def limpieza_archivo():
    """
    Programa para poner en blanco un archivo random
    Hecho por GB
    """
    archivo = open("00- puntajes_juego.csv", "w")
    archivo.close()

    return 



def inicializar_puntaje_usuarios(nombres_pos_palabraClave, puntos, letras_B, letras_M):
    """
    Función que carga : posicion,jugador,palabra_elegida,puntos,letras_buenas,letras_malas en un csv para poder jugar la interfaz
    Creada por GB 
    """

    registro = open("00- puntajes_juego.csv", "w")
    # Leer títulos
    # inea = registro.readline()

    # Escribir en el archivo según ordenamiento establecido en el contrato de la función
    for i in sorted(nombres_pos_palabraClave, key = lambda i : nombres_pos_palabraClave[i]):
        registro.write(f"{nombres_pos_palabraClave[i][0]},{i},{nombres_pos_palabraClave[i][1]},{puntos},{letras_B},{letras_M}\n")

    # print(nombres_pos_palabraClave)

    registro.close()
    return None

def cargar_datos_iniciales(nombres_pos_palabraClave, puntos, letras_B, letras_M):
    """
    Función que carga los datos en un array de lista \n
    Devuelve una lista de listas, con la posición\n
    Hecha por GB
    """
    jugadores_palabra_puntaje = []

    for i in sorted(nombres_pos_palabraClave, key = lambda i : nombres_pos_palabraClave[i]):
        jugadores_palabra_puntaje.append([nombres_pos_palabraClave[i][0],i,nombres_pos_palabraClave[i][1],puntos,letras_B,letras_M])
        # print(jugadores_palabra_puntaje)


    return jugadores_palabra_puntaje



def iterar_multijuego(jugadores_posiciones_puntajes):
    """Función que toma realiza la lógica de juego multilinea\n 
    Hecha por GB
    """

    # print(f"Jugadores _ POSIONES _ PUNTAJES = {jugadores_posiciones_puntajes}")
    
    # jugadores_por_posicion = devolver_lista_jugadores()
    excluidos = []
    cant_jugadores = int(len(jugadores_posiciones_puntajes))
    # print(f"LA CANTIDAD DE JUGADORES ES {cant_jugadores}")
    # archivo = open("00- puntajes_juego.csv")
    llave_1 = False
    i = 0
    max_movimientos =  120
    llave_2 = 0
    while llave_1 != True and llave_2 < max_movimientos:

        perfil_jugador = jugadores_posiciones_puntajes[i]
        print(perfil_jugador) # Bloquear posición recordar
        if perfil_jugador:
            if (perfil_jugador[1]) in excluidos:
                pass
            else:
                resultados_evaluar = jugar_multijugador_lista(perfil_jugador)

                if len(resultados_evaluar) == 7:
                    if resultados_evaluar[6] == 3 or resultados_evaluar[6] == 2:
                        excluidos.append(resultados_evaluar[1])
                        if len(excluidos) == cant_jugadores:
                            print("\n\n\nGANO LA MAQUINA \n\n\n")
                            jugadores_posiciones_puntajes.append([100, "Maquina", "", 100, "","",""])
                            llave_1 = True
                    elif resultados_evaluar[6] == 1:
                        jugadores_posiciones_puntajes[i]  = resultados_evaluar
                        llave_1 = True
                elif len(resultados_evaluar) == 6:
                    jugadores_posiciones_puntajes[i] = resultados_evaluar
                    pass

        i += 1

        if i == (cant_jugadores):
            i = 0
        llave_2 += 1

    return jugadores_posiciones_puntajes 
   

def obtener_maximo(lista):
    #ELEMENTO 3 de lista es el puntaje
    maximo = -100

    lista_puntaje = []
    for i in range (len(lista)):
        if int(lista[i][3]) > maximo:
            lista_puntaje.append(lista[i][3])


    return lista_puntaje


def ordenar_lista(podio):

    # print(f"Ingreso al podio {podio}")

    devolver = {}
    for i in range (len(podio)):
        # print(f" {podio[i][0]} {podio[i][1]} {podio[i][2]}" )
        devolver[podio[i][1]] = [podio[i][2],int(podio[i][3]), podio[i][4], podio[i][5] ]

    # print(devolver)       
    return devolver



def acumular_valores_partidas(podio):

    print(f"\nIngreso al podio {podio}")

    devolver = {}
    for i in range (len(podio)):
        # print(f" {podio[i][0]} {podio[i][1]} {podio[i][2]}" )
        devolver[podio[i][1]] = [[podio[i][2],int(podio[i][3]), podio[i][4], podio[i][5] ]]
    
    # print(devolver)       
    return devolver



def cargar_datos_en_archivo_ganador_partida(podio):
    archivo = open("00- puntajes_juego.csv", "w")

    print(f"\n\n\n{podio}\n\n\n")

    for i in sorted(podio, key = lambda i : podio[i][1], reverse = True):
        archivo.write(f"{podio[i][0]},{podio[i][1]},{podio[i][2]},{podio[i][3]},{podio[i][4]},{podio[i][5]}\n ")

    archivo.close
    return None


def imprimir_tabla_ganador(podio):

    print(f" \n\n\n PODIO \n {podio}\n")
    
    for i in sorted(podio, key = lambda i : podio[i][1], reverse = True):
        print(f"{i} {podio[i]} ")
    
    return None



def jugar_multijugador_lista(perfil_jugador):

    pos,jugador, palabraElegida, puntaje_total, letrasBuenas, letrasMalas = perfil_jugador
    # print(" Los valores son: {0}, {1}, {2}, {3}, {4}, {5}".format(pos,jugador, palabraElegida, puntaje_total, letrasBuenas, letrasMalas))
    aciertos = evaluar_puntaje_incial(letrasBuenas)
    # print(f"LOS ACIERTOS INGRESADOS DAN: {aciertos}")
    errores = evaluar_puntaje_incial(letrasMalas)

    # print(f"LOS ERRORES INGRESADOS DAN {errores}")
    contador = int(len(letrasMalas))


    letrasBuenas = correccion_letras(letrasBuenas)
    # print(f"\nletras buenas {letrasBuenas}\n")
    letrasMalas = correccion_letras(letrasMalas)


    puntos_por_acierto = 2
    total_puntajes_ganados = int(aciertos*(puntos_por_acierto))
    puntos_por_desaciertos = -1
    total_puntajes_perdidos = int(errores*(puntos_por_desaciertos))
    puntaje_total =  total_puntajes_ganados - total_puntajes_perdidos
    # print(f"El puntaje total tiene que ser 0: {puntaje_total}")
    
    cant_intentos = 7
    puntaje = Asignacion_Puntajes(total_puntajes_ganados, total_puntajes_perdidos)
    muestraParcial = muestraPalabraEncriptada(letrasBuenas, palabraElegida)

    # print(f"\n\n EL PERFIL DEL JUGADOR QUE ENTRO ES: {perfil_jugador}")

    print("ES EL TURNO DE:{0:8}".format(jugador.upper()))
    print(f"Palabra a adivinar: {muestraParcial.upper()}  Aciertos: {aciertos} - {letrasBuenas} Desaciertos: {errores} - {letrasMalas}\n\n\n")

    # llave_2 para poder salir del else con la modificación de la parte10
    llave_2 = False
    punteo_error = 0

    # prueba para evitar el bug que se genera cuando perdes y no tiene almacenado los datos de la lista a pasar.

    lista_pasar = [int(pos), str(jugador), str(palabraElegida), str(puntaje), str(letrasBuenas), str(letrasMalas)]

    while contador <= cant_intentos and llave_2 != True:

        salidaLetra = letraValida(letrasBuenas, letrasMalas)
        letra = salidaLetra[0] 
        sigueJugando = salidaLetra[1]

        if sigueJugando:

            esBuena = letraBuena(letra, palabraElegida)

            if esBuena:
                aciertos += 1
                total_puntajes_ganados = int(aciertos * puntos_por_acierto)
                puntaje = Asignacion_Puntajes( total_puntajes_ganados, total_puntajes_perdidos)
                letrasBuenas = acumularLetras(letra, letrasBuenas)
                muestraParcial = muestraPalabraEncriptada(letrasBuenas, palabraElegida)
                printeoAciertoError(letra, muestraParcial, aciertos, errores, palabraElegida, letrasMalas)
                contador = ganaPierdo_multilinea(muestraParcial, palabraElegida, errores,puntaje)
                if contador == 9:
                    puntaje += 10
                # pos,jugador, palabraElegida, puntaje_total, letrasBuenas, letrasMalas = lista_pasar 

                # Cuando me equivoco, hay que actualizar los datos que están en la primer base de datos.



                print(f"Habria que almacenar estos datos o redefinirlos en el juego {pos} {jugador} {palabraElegida} {puntaje} {letrasBuenas} {letrasMalas} ")
                lista_pasar = [int(pos), str(jugador), str(palabraElegida), str(puntaje), str(letrasBuenas), str(letrasMalas)]
                # print(f"El puntaje total es: {puntaje}")
                                   
            elif letra not in letrasMalas: 
                punteo_error += 1
                errores += 1    
                total_puntajes_perdidos = punteo_error * puntos_por_desaciertos
                puntaje = Asignacion_Puntajes(total_puntajes_ganados, total_puntajes_perdidos)
                letrasMalas = acumularLetras(letra, letrasMalas)
                muestraParcial = muestraPalabraEncriptada(letrasBuenas, palabraElegida)
                printeoAciertoError(letra, muestraParcial, aciertos, errores, palabraElegida, letrasMalas)

                lista_pasar = [int(pos), str(jugador), str(palabraElegida), str(puntaje), str(letrasBuenas), str(letrasMalas)]
                print(f"LA LISTA A PASAR ES {lista_pasar} y el contador vale : {errores}")

                if errores == 8:
                    puntaje -= 5
                elif errores == 7:
                    lista_pasar = [int(pos), str(jugador), str(palabraElegida), str(puntaje), str(letrasBuenas), str(letrasMalas)]
                    # print("\n\n\n ULTIMA CHANCE \n\n\n")


                # pos,jugador, palabraElegida, puntaje, letrasBuenas, letrasMalas
                llave_2 = True

            else:
                print("LETRA REPETIDA")
                lista_pasar = [int(pos), str(jugador), str(palabraElegida), str(puntaje), str(letrasBuenas), str(letrasMalas)]

        else:
            lista_pasar = [int(pos),str(jugador),str(palabraElegida),str(puntaje_total),str(letrasBuenas),str(letrasMalas)]
            contador = 10
            print("HAS ABANDONADO LA PARTIDA \n")

        # print (f"LLEGO A ESTE INTERVALO LOS ERRORES SON {errores}")    
        
        if contador == 9:
            lista_pasar.append(1)
        elif errores == 8:
            lista_pasar = [int(pos), str(jugador), str(palabraElegida), str(puntaje), str(letrasBuenas), str(letrasMalas)]
            lista_pasar.append(2)
        elif contador == 10:
            lista_pasar.append(3)
    
 

    return lista_pasar

def devolver_lista_jugadores():
    jugadores = []
    archivo = open("00- puntajes_juego.csv")
    linea = lineas(archivo)
    fin_archivo = "999"

    while linea[0] != fin_archivo:
        jugadores.append(lineas[1])
        lineas = lineas(archivo)
    
    return jugadores



def cargar_datos_perdedor_abandono(lista_podios, usuario):
    lista_podios.append(usuario)        
    return lista_podios    

def cargar_datos_ganador(): # PODRIA RECIBIR UN PARAMETRO CON UN BLOQUE IF 
    """
    Toma los datos una vez que se encuentra al ganador(equipo o máquina)\n
    devuelve una lista para imprimir\n
    Hecha por GB
    
    """
    archivo = open("00- puntajes_juego.csv")
    # Lineas devuelve: posición _ jugador _ palabraClave _ puntaje _ aciertos _ errores
    posicion, jugador, palabra_adivinar, puntaje_total, aciertos, errores = lineas(archivo)
    max = "999"
    podio = {}
    puntos = []
    puntaje_total = int(puntaje_total)

    while posicion != max:
        podio[jugador] = [puntaje_total, palabra_adivinar, aciertos, errores]
        puntos.append(puntaje_total)
        posicion, jugador, palabra_adivinar, puntaje_total, aciertos, errores = lineas(archivo)

    archivo.close()

    return puntos,podio

def imprimir_ganador(puntos, podio):

    # print(f"\n\n\n\n PODIO ORDENADO \n {podio}\n\n\n")

    valor = -100

    for i in puntos:
        if int(i) > valor:
            valor = int(i)

    # print(valor)
    ganador = []

    for i in sorted(podio, key = lambda i: int(podio[i][1]), reverse = True):
        if int(podio[i][1]) == valor:
            print("El ganador es: {0:1}, puntaje de: {1:2}, palabra: {2:3}, aciertos: {3:4}, errores: {4:5}\n\n". format(i, podio[i][1], podio[i][0], podio[i][2],podio[i][3]))
            ganador = [i, podio[i][1], podio[i][0], podio[i][2],podio[i][3]]
        else:
             print("Jugador: {0:1}, puntaje de: {1:2}, palabra: {2:3}, aciertos: {3:4}, errores: {4:5}". format(i, podio[i][0], podio[i][1], podio[i][2],podio[i][3]))
    
    return ganador 

def gano_maquina(puntos,podio):
    print("LA MAQUINA HA GANADO \n Los jugadores quedaron como:")

    
    for i in puntos:
        if int(i) > valor:
            valor = int(i)

    # print(valor)

    for i in sorted(podio, key = lambda i: int(podio[i][0]), reverse = True):
        print("Jugador: {0:1}, puntaje de: {1:2}, palabra: {2:3}, aciertos: {3:4}, errores: {4:5}". format(i, podio[i][0], podio[i][1], podio[i][2],podio[i][3]))
    
    return None



def eliminar_perfil_jugador(lista):
    # Elimina el jugador indicado: 

    jugador_eliminado = lista [1]

    # print(lista)
    file_agregar_eliminados = open("00- puntajes_juego_eliminados.csv", "a")
    file_agregar_eliminados.write(f"{lista[0]},{lista[1]},{lista[2]},{lista[3]},{lista[4]},{lista[5]}\n")

    file_agregar_eliminados.close()

    print(f"Jugador a Eliminar: {jugador_eliminado}")
    lista_jugadores = []

    archivo = open("00- puntajes_juego.csv") 
    linea = lineas_unica(archivo)
    # print(linea)
    max = "999"
    while linea != max:
        nombre = linea
        lista_jugadores.append(nombre)
        linea = lineas_unica(archivo)
    print("lista_jugadores :  {}".format(lista_jugadores))
    archivo.close()

    # print(f"La lista de nombres es: {lista_jugadores}")

    with open("00- puntajes_juego.csv", "w") as file:
        for i in range (len(lista_jugadores)):
            
            if lista_jugadores[i] == jugador_eliminado:
                pass
            else:
                file.write(f"{lista_jugadores[i]}\n")

    return None

def lineas_unica(archivo):

    linea = archivo.readline()
    if linea:
        devolver = linea.rstrip("\n")
    else:
        devolver = "999"

    return devolver    

def pisar_puntajes(lista):
    """
    Recibe como parámetros los datos del jugador si: \n
    Se equivocó, si quiso dejar de jugar, si ganó \n
    Pisa el archivo en la linea correspondiente\n
    Hecha por GB 
    """
    # pos,jugador, palabraElegida, puntaje_total, letrasBuenas, letrasMalas = lista
    
    archivo = open("00- puntajes_juego.csv", "r")
    
    lista_maestra = []
    linea = lineas(archivo)
    max = "999"
    while linea[0] != max:
        if linea[0] == lista[0]:
            lista_maestra.append(lista)
        else:
            lista_maestra.append(linea)
        linea = lineas(archivo)

    archivo.close()

    # print(f"lista maestra: {lista_maestra}")


    archivo = open("00- puntajes_juego.csv", "w") # Abriendo archivo para poder pisarlo
 
    for i in range (len(lista_maestra)):
        archivo.write(f"{lista_maestra[i][0]},{lista_maestra[i][1]},{lista_maestra[i][2]},{lista_maestra[i][3]},{lista_maestra[i][4]},{lista_maestra[i][5]}\n")
    
    archivo.close()

    return None
       

def capturar_linea(renglon):

    """Abre los puntajes y captura un renglon\n
    devuelve una cadena\n
    Hecha por GB
    """
    archivo = open("00- puntajes_juego.csv")
    linea = lineas(archivo)
    i = 0
    while i < renglon:
        devolver = linea
        linea = lineas(archivo)
        i += 1
    
    # print(devolver)
    archivo.close()

    return devolver


def posicionar_en_cero():
    archivo = open("00- puntajes_juego.csv")
    archivo.seek(0)
    archivo.close
    return
  
def cargar_datos_puntaje(lista_juego):

    print(lista_juego)
    # archivo = open("00- puntajes_juego_parciales", "a")
    ## ULTIMO CAMBIO
    # archivo.close()
    print("has salido")
    return None


def leer_archivo_con_posicionador(contador):

    """
    Programa que corrije el bug que se genera al reescribir el archivo 00- puntajes_juego
    posiciona la linea de parametros según corresponda el orden
    Hecho por GB
    """
    archivo = open("00- puntajes_juego.csv", "r+")

    for i in range (contador):
        linea = archivo.readline()
    archivo.close()

    return None


def lineas(archivo):
    """
    Programa que lee los archivos
    Hecho por GB
    """
    linea = archivo.readline()
    if linea:
        devolver = linea.rstrip("\n").split(",")
    else:
        devolver = ["999","DEVOLVER","","0","",""]
    
    archivo.close()

    return devolver
# agregando comentario

def cargar_datos_puntajes_juego(lista):
    """
    Recibe como parámetros los datos del jugador si: \n
    Se equivocó, si quiso dejar de jugar, si ganó \n
    Los carga en un archivo temporal\n
    Hecha por GB 
    """
    pos,jugador, palabraElegida, puntaje_total, letrasBuenas, letrasMalas = lista

    lista_maestra = []
    archivo = open("00- puntajes_juego.csv", "r")

    linea = lineas(archivo)
    max = "999"
    while linea[0] != max:
        if linea[0] == lista[0]:
            lista_maestra.append(lista)
        else:
            lista_maestra.append(linea)
        linea = lineas(archivo)
    archivo.close()

    # print(f"lista maestra: {lista_maestra}")

    # ABRO EL ARCHIVO PARA PISARLO
    archivo = open("00- puntajes_juego.csv", "w") ########### 
 
    for i in range (len(lista_maestra)):
        archivo.write(f"{lista_maestra[i][0]},{lista_maestra[i][1]},{lista_maestra[i][2]},{lista_maestra[i][3]},{lista_maestra[i][4]},{lista_maestra[i][5]}\n")
    
    archivo.close()
   
    # print(lista_maestra)
    # print(type(pos))
    # print("llegaste hasta donde querias")

    return None

    

def evaluar_puntaje_incial(letra):
    # me va a dar cero solo la primera vez, hago un bloque para solventarlo

    if len(letra) > 0:
        devolver = len(letra) 
    elif len(letra) == 0:
        devolver = 0
    elif letra == "0":
        devolver = 0
    else:
        devolver = 0
    return devolver

def correccion_letras(letra):
    # corrigiendo bug inicial
    if letra == "0":
        devolver = ""
    elif letra == "": # ampliación para mejorar bug
        devolver = ""
    else:
        devolver = letra
    return devolver


def ganaPierdo_multilinea(muestraParcial, palabraAhorcado, contadorErrores,puntaje):

    if muestraParcial == palabraAhorcado:
        contadorErrores = 9
        # print("puntaje: {0}".format(puntaje))
        puntaje = int(puntaje) + 10
        print(f"\nHAS GANADO! SU PUNTAJE ES: {puntaje}\n")
        # nueva_partida(puntaje)
    elif contadorErrores == 8:
        print(f"\nPERDISTE! SU PUNTAJE ES: {puntaje}\n")
        # print(puntaje)
        puntaje = int(puntaje) - 5
    else:
        pass
    return contadorErrores

def agregar_gandores_perdedores(contador, lista_pasar):

    return None

##########---------------------------------------------- FUNCIONES FINALIZADORAS --------------------------------------------###############

def limpiar_ingresos():
    """Funcion que abre el archivo ingresos\n
    GB"""
    archivo = open("00- ingresos.csv", "w")

    archivo.close()


def capturar_ganador(lista):

    puntaje = []

    # CORRIGIENDO ESPACIOS VACIOS
    for i in range (len(lista)):
        if lista[i][3] == "":
            lista[i][3] = 0
        else:
            lista[i][3] = int(lista[i][3])


    for i in range (len(lista)):
        puntaje.append(lista[i][3])


    maximo = max(puntaje)

    # print(maximo)
    # print(puntaje)

    maximo = int(maximo)

    ganador = ""

    for i in range (len(lista)):
        if int(lista[i][3]) == maximo:
            ganador = str(lista[i][1])

    # print(f"El ganador es: \n\n{ganador}\n\n")

    # print(lista)

    return ganador

##########--------------------------------------------- BLOQUE QUE SERIA EL NUEVO MAIN ------------------------------------- #############################

def ingresar_etapa_ocho():

    # crear_ventana_de_inicio()
    jugadores = asignar_turnos_a_todos_los_jugadores()
    # print(jugadores.items())
    longitud = validez_longitud()
    if longitud == "": 
        longitud = int(randint(5,9))
    # print(f"la longitud es {longitud}")
    # palabra = elegir_palabra(longitud)

    # PROGRAMA QUE ME IMPRIME LAS POSICIONES Y LAS PALABRAS:

    definir_nombre_variable = consolidar_posiciones_y_palabras(jugadores, longitud)

    return definir_nombre_variable


def correr_etapa_9():
    # crear_ventana_de_inicio()
    nombres_posiciones_palabraClave = ingresar_etapa_ocho()
    # print(f"Los nombres, posiciones y las palabras claves son: {nombres_posiciones_palabraClave}")
 
    puntos = letras_buenas = letras_malas = ""
    lista_jugadores_puntos = cargar_datos_iniciales(nombres_posiciones_palabraClave,puntos,letras_buenas ,letras_malas)

    jugadores_posiciones_puntajes = iterar_multijuego(lista_jugadores_puntos)

    podio_ordenado = ordenar_lista(jugadores_posiciones_puntajes)
    lista_puntajes = obtener_maximo(jugadores_posiciones_puntajes)
    ganador = imprimir_ganador(lista_puntajes, podio_ordenado)

    print(f"THE WINNER IS:   \n\n {ganador[0]}")
    print("Jugamos otra vez???")
    # inicializar_puntaje_usuarios(nombres_posiciones_palabraClave,puntos,letras_buenas ,letras_malas )
    # jugar_multijugador()

    #cargando los registros para poder inicializar el juego.

    return None

# correr_etapa_9()



def bloque_principal_juego():

    partidas = 0
    ganador_ronda = ""

    i = False # llave de control de iteraciones

    while i != True:

        #### verifico si hay que limpiar o no los registros. 
        ### posible mejora de código incoportando consultas como: eliminar jugador 
        if partidas == 0 and ganador_ronda == "":
            # limpiar_ingresos()
            crear_ventana_de_inicio()
        else:
            pass

        if partidas == 0 or ganador_ronda == "Maquina":
            jugadores = asignar_turnos_a_todos_los_jugadores()
        else:
            jugadores = asignar_turnos_a_todos_los_jugadores_menos_ganador(ganador_ronda)

        longitud = validez_longitud()

        if longitud == "":
            longitud = int(randint(5,9))
        
        # Función que carga los datos para poder inicializar el juego
        lista_jugadores_puntos = cargar_datos_inicio_juego(jugadores, longitud)

        jugadores_posiciones_puntajes = iterar_multijuego(lista_jugadores_puntos)

        # print(f"\n\n\n\n JUGADORES_ POSICIONES _ PUNTAJES _ ALMACENAR EN UN DICCIONAR \n\n\n {jugadores_posiciones_puntajes}")

        ganador_ronda = capturar_ganador(jugadores_posiciones_puntajes)

        # definir función que pise los valores del jugador, en la lista del juego.

        podio_ordenado = ordenar_lista(jugadores_posiciones_puntajes)

        # print(f"podio ordenado: \n{podio_ordenado}")


        lista_puntajes = obtener_maximo(jugadores_posiciones_puntajes)
        ganador= imprimir_ganador(lista_puntajes, podio_ordenado)

        # print(f"ganadores es : {ganador}")

        # print(ganador)
        if partidas == 0:
            # Genero el diccionario que acumula las posiciones
            acumulador_puntajes_por_usuario = acumular_valores_partidas(jugadores_posiciones_puntajes)
        else:
            acumulador_puntajes_varias_partidas = adosar_valores_partidas(acumulador_puntajes_por_usuario, jugadores_posiciones_puntajes)

        
        if partidas == 0:
            print(acumulador_puntajes_por_usuario)
        else:
            print(acumulador_puntajes_varias_partidas)


        partidas += 1

        consulta = input("Desea seguir jugando??? \nSI (cualquier tecla)\nNO(escriba esc o 0")
        if consulta == "esc" or consulta == "0":
            i = True

    return None


def adosar_valores_partidas(acumulador_puntajes_por_usuario, jugadores_posiciones_puntajes):

    print(acumulador_puntajes_por_usuario)
    print(f"Hay que combinar las posiciones estás {jugadores_posiciones_puntajes}")

    for clave in range (len(acumulador_puntajes_por_usuario)):
        for jugador in jugadores_posiciones_puntajes:
            if clave == jugador[1]:
                acumulador_puntajes_por_usuario[clave].append([jugador[2], int(jugador[3]),jugador[4], jugador[5]])
    
    for i in sorted(acumulador_puntajes_por_usuario, key = lambda i : acumulador_puntajes_por_usuario[i][1], reverse = True):
        





    return None

def cargar_datos_inicio_juego(jugadores, longitud):

    nombres_posiciones_palabraClave = consolidar_posiciones_y_palabras(jugadores, longitud)
    puntos = letras_buenas = letras_malas = ""
    lista_inicial = cargar_datos_iniciales(nombres_posiciones_palabraClave,puntos,letras_buenas ,letras_malas)

    return lista_inicial


bloque_principal_juego()







