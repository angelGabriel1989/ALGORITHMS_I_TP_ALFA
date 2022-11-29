import TPAL001A
from TPAL001A import validez_longitud, diccionarValido, eligePorCantidad, randomPalabraElegida


longitud = int(validez_longitud())

def elegir_palabra(longitud):
    "Gabriel Barros"
    lista_diccionario = diccionarValido()
    lista_Igualdad_Caracteres = eligePorCantidad(longitud, lista_diccionario)
    palabraElegida = randomPalabraElegida(lista_Igualdad_Caracteres)
    return palabraElegida

palabra = elegir_palabra(longitud)





print(palabra)