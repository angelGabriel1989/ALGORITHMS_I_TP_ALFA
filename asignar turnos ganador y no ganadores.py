def contar_jugadores():
    #Observacion=esta funcion ya esta en la interfaz solo que lo agregue aca para correr todo teniendo el archivo ingresos.csv con sus jugadores y fijarme que me devuleva todo okey
    #Cuenta la cantidad de jugadores que ingresaron a la sala de juego una vez que se presiono el boton iniciar partida
    contador_jugadores=0
    with open("00- ingresos.csv", "r",newline="") as file:
        linea = file.readline()
        while linea != "":
            contador_jugadores=contador_jugadores+ 1
            linea = file.readline()
    return(contador_jugadores)


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
    return diccionario_jugadores_con_turnos


def leer_linea(archivo_a_estudiar):
    linea=archivo_a_estudiar.readline()
    if linea != "":
        devolver=linea.rstrip().split(",")
    else:
        devolver=[" "]
    return devolver


print(asignar_turnos_a_todos_los_jugadores_menos_ganador("Gaby_2007"))