from Lib import random
from Lib import string


#ej2

def contar_palabras(cadena):
    palabras = cadena.split( )
    return len(palabras)

#ej6

def contar_ocurrencias(frases):
    palabras = ["música", "charla ", "entretenimiento"]
    contador = {palabra: 0 for palabra in palabras}
    for frase in frases:
        for palabra in palabras:
            if palabra in frase.lower():
                contador[palabra] += 1
    return contador

#ej7

def crear_codigo(nombre,fecha):
    cant = len(nombre) + len(fecha)
    if(len(nombre)<16):
        chars = string.ascii_uppercase + string.digits
        codigo = nombre + " - " + fecha + " - "
        largo = 30 - cant
        for _ in range(largo):
            codigo = codigo + random.choice(chars)
        return codigo
    return "Se debe ingresar un usuario que no exeda los 15 caracteres"

#ej8

def son_anagramas(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)


#ej10

def actualizar_ronda(round,ronda):
    KILL = 3
    ASISTENCIA = 1
    MUERTE = -1
    max = -99
    for jugador, stats in round.items():
        murio = 1 if stats['deaths'] else 0
        ronda[jugador]['kills'] += stats['kills']
        ronda[jugador]['assists'] += stats['assists']
        ronda[jugador]['deaths'] += murio
        puntos = stats['kills'] * KILL + stats['assists']* ASISTENCIA + murio*MUERTE
        ronda[jugador]['puntos'] += puntos
        if(puntos>max):
            max = puntos
            mvp = jugador
    return mvp


def imprimir_ronda(ronda,ronda_n,mvp):
    print(f"\nTabla de clasificación - Ronda: {ronda_n}")
    print("Jugador K A D P MVPs")
    print("-------------------")
    for jugador, dato in ronda:
        print(f"{jugador} {dato['kills']} {dato['assists']} {dato['deaths']} {dato['puntos']} {dato['MVPs']}")
    print(f"\nMVP de la ronda: {mvp}")


def puntos_ronda(item):
    return item[1]['puntos']
