import random
import lectores
import gamelib

ARCHIVO_POKEMONES = 'pokemons.csv'
ARCHIVO_DETALLE_MOVIMIENTOS = 'detalle_movimientos.csv'
ARCHIVO_TABLA_TIPOS = 'tabla_tipos.csv'

MENSAJE_ELIJA_PROX_COMBATIENTE = 'Ingrese el número del pokemon que luchará a continuación: {}'
MENSAJE_ERROR_ELECCION_PROX_COMBATIENTE = 'No eligió correctamente su pŕoximo combatiente. Inténtalo de nuevo'
MENSAJE_ELIJA_MOVIMIENTO = 'Elija que movimiento usará {} en este turno. Tienes disponibles: {}'
MENSAJE_ERROR_ELECCION_MOVIMIENTO = 'No eligió correctamente su pŕoximo movimiento. Inténtalo de nuevo'
MENSAJE_MUY_EFECTIVO = 'El ataque de {} a {} es super-efectivo!'
MENSAJE_POCO_EFECTIVO = 'El ataque de {} a {} es poco efectivo.'
MENSAJE_NADA_EFECTIVO = 'El ataque de {} a {} no es efectivo!'
MENSAJE_NORMAL_EFECTIVO = 'El ataque de {} a {} es efectivo.'
MENSAJE_MOV_NO_MODELADO = 'Uno de los movimientos elegidos no está modelado en el juego.'
MENSAJE_CURACION = '{} recupera parte de su salud.'
MENSAJE_STAT_NERF = '{} sufre un stat nerf.'
MENSAJE_STAT_BOOST = '{} gana un stat boost.'
GANO_JUGADOR_1 = 'Felicidades, ganó el jugador 1!'
GANO_JUGADOR_2 = 'Felicidades, ganó el jugador 2!'

def color_barra(porcentaje):
    """Cambia el color de la barra de salud"""
    if porcentaje >= 0.8:
        color = 'green'

    if 0.3 < porcentaje < 0.8:
        color = 'orange'
        
    if porcentaje <= 0.3:
        color = 'red'
    
    return color


def quien_primero(combatiente1, combatiente2):
    """
    Recibiendo los dos combatientes, decide cuál mueve primero según cuál tiene mayor velocidad.
    Si las velocidades son iguales, elige aleatoriamente.
    Retorna el entero del combatiente.
    """
    if combatiente1.velocidad > combatiente2.velocidad:
        return 1
    elif combatiente1.velocidad < combatiente2.velocidad:
        return 2
    elif combatiente1.velocidad == combatiente2.velocidad:
        aleatorio = random.choice((1, 2))
        return aleatorio
    else: raise Exception ('Error en función quien_primero()')


def numero_a_nombre(nro, archivo):
    """
    Recibe el número de un pokemon y retorna su nombre en string.
    """
    info = lectores.lector_por_numero(nro, archivo)

    return info['nombre']


def jugador_elige_pokemon(equipo):
    """
    Recibe una lista de pokemones de todo el equipo que puede elegir el usuario
    y retorna el que elija el usuario.
    """
    lista_en_nombres = []
    for par in equipo.pokmov:
        lista_en_nombres.append((numero_a_nombre(par[0], ARCHIVO_POKEMONES), par[0]))

    while True:
        ingreso = gamelib.input(MENSAJE_ELIJA_PROX_COMBATIENTE.format(lista_en_nombres))
        for par in equipo.pokmov:
            if ingreso in par:
                return par
        gamelib.say(MENSAJE_ERROR_ELECCION_PROX_COMBATIENTE)


def jugador_elige_movimiento(combatiente):
    """
    Recibe una lista de todo el equipo y un numero de pokemon
    y retorna el movimiento que elegió el usuario para ese pokemon
    """
    eleccion = ''

    while eleccion == '':
        ingreso = gamelib.input(MENSAJE_ELIJA_MOVIMIENTO.format(combatiente.nombre, combatiente.movimientos))
        if ingreso == None:
            gamelib.say(MENSAJE_ERROR_ELECCION_MOVIMIENTO)
            continue
        if ingreso in combatiente.movimientos:
            eleccion = ingreso
        else: gamelib.say(MENSAJE_ERROR_ELECCION_MOVIMIENTO)

    return eleccion