import lectores
import gamelib
import random

ANCHO_VENTANA = 900
ALTO_VENTANA = 600

ARCHIVO_POKEMONES = 'pokemons.csv'
ARCHIVO_DETALLE_MOVIMIENTOS = 'detalle_movimientos.csv'
ARCHIVO_TABLA_TIPOS = 'tabla_tipos.csv'

MENSAJE_ELIJA_PROX_COMBATIENTE = 'Ingrese el número del pokemon que luchará a continuación: {}'
MENSAJE_ERROR_ELECCION_PROX_COMBATIENTE = 'No eligió correctamente su pŕoximo combatiente. Inténtalo de nuevo'
MENSAJE_ELIJA_MOVIMIENTO = 'Elija que movimiento usará {} en este turno. Tienes disponibles: {}'
MENSAJE_ERROR_ELECCION_MOVIMIENTO = 'No eligió correctamente su pŕoximo movmiento. Inténtalo de nuevo'

class Combatiente:
    def __init__(self, numero, archivo):
        stats = lectores.lector_por_numero(numero, ARCHIVO_POKEMONES)
        self.numero = int(stats[0])
        self.imagen = stats[1]
        self.nombre = stats[2]
        self.tipos = stats[3]
        self.hp = int(stats[4]) + 110
        self.ataque = int(stats[5])
        self.defensa = int(stats[6])
        self.speat = int(stats[7])
        self.spedf = int(stats[8])
        self.velocidad = int(stats[9])
        self.movimientos = lectores.movimiento_en_pokemon(numero, archivo)

    def esta_vivo(self):
        if self.hp > 0:
            return True
        else: return False

    def reemplazar(self, numero, archivo):
        stats = lectores.lector_por_numero(numero, ARCHIVO_POKEMONES)
        self.numero = stats[0]
        self.imagen = stats[1]
        self.nombre = stats[2]
        self.tipos = stats[3]
        self.hp = stats[4] + 110
        self.ataque = stats[5]
        self.defensa = stats[6]
        self.speat = stats[7]
        self.spedf = stats[8]
        self.velocidad = stats[9]
        self.movimientos = lectores.movimiento_en_pokemon(numero, archivo)

    def informacion(self):
        return self.numero, self.imagen, self.nombre, self.tipos, self.hp, self.ataque, self.defensa, self.speat, self.spedf, self.velocidad


def numero_a_nombre(nro):
    """
    Recibe el número de un pokemon y retorna su nombre en string.
    """
    info = lectores.lector_por_numero(nro, ARCHIVO_POKEMONES)
    #print ('57 |', info)
    return info[2]


def jugador_elige_pokemon(lista):
    """
    Recibe una lista de pokemones de todo el equipo que puede elegir el usuario
    y retorna el que elija el usuario.
    """
    lista_en_nombres = []
    for i in range (len(lista)):
        #print ('68 |', lista[i])
        lista_en_nombres.append([numero_a_nombre(int(lista[i])), lista[i]])

    eleccion = ''
    while eleccion == '':
        ingreso = gamelib.input(MENSAJE_ELIJA_PROX_COMBATIENTE.format(lista_en_nombres))
        if ingreso in lista:
            eleccion = ingreso
        else: gamelib.say(MENSAJE_ERROR_ELECCION_PROX_COMBATIENTE)

    return eleccion


def jugador_elige_movimiento(lista, numero):
    """
    Recibe una lista de todo el equipo y un numero de pokemon
    y retorna el movimiento que elegió el usuario para ese pokemon
    """
    eleccion = ''
    indice_pokemon = lista.index(numero)
    opciones = lista[indice_pokemon + 1]

    while eleccion == '':
        ingreso = gamelib.input(MENSAJE_ELIJA_MOVIMIENTO.format(numero_a_nombre(numero), opciones))
        if ingreso in opciones:
            eleccion = ingreso
        else: gamelib.say(MENSAJE_ERROR_ELECCION_MOVIMIENTO)
    return eleccion


def calculadora_daño():
    """
    Hace todos los calculos de daño, retorna el numero de daño hecho.
    """
    pass


def calculadora_efecto():
    """
    Hace todos los calculos de stat boost, retorna los efectos.
    """
    pass


def calculadora_sanacion():
    """
    Al ser llamada, calcula cuánto debe ser sanado un pokemon.
    """
    pass


def quien_primero(combatiente1, combatiente2):
    """
    Recibiendo los dos combatientes, decide cuál mueve primero según cuál tiene mayor velocidad.
    Si las velocidades son iguales, elige aleatoriamente.
    Retorna el entero del combatiente.
    """
    info1 = combatiente1.informacion()
    info2 = combatiente2.informacion()
    if info1[9] > info2[9]:
        return 1
    elif info1[9] < info2[9]:
        return 2
    elif info1 == info2:
        aleatorio = random.choice((1, 2))
        return aleatorio
    else: raise Exception ('Error en función quien_primero()')


def dibujar_combate(combatiente1, combatiente2, equipo_1, equipo_2, vivos_1, vivos_2):
    """
    Dibuja el estado del combate al principio del turno, para que los usuarios puedan elegir que hacer a continuación según
    cómo ven que están sus pokemones en juego.
    """
    VACIO = 0
    FRANJA_AZUL_Y = 88
    TITULO_Y = 70
    COLOR_AZUL = '#0d1364'
    MITAD_X = ANCHO_VENTANA // 2
    ANCHO_RECTANGULO_HP = 80

    info_combat_1 = combatiente1.informacion()
    info_combat_2 = combatiente2.informacion()
    #print ('154 | ', info_combat_1, info_combat_2)
    #print ('155 | ', info_combat_1[0])
    hp_combat_1_entera = int(lectores.lector_por_numero(info_combat_1[0], ARCHIVO_POKEMONES)[4]) + 110
    hp_combat_2_entera = int(lectores.lector_por_numero(info_combat_2[0], ARCHIVO_POKEMONES)[4]) + 110
    hp_combat_1_actual = info_combat_1[4]
    hp_combat_2_actual = info_combat_2[4]
    hp_pocentaje_1 = hp_combat_1_actual // hp_combat_1_entera
    hp_pocentaje_2 = hp_combat_2_actual // hp_combat_2_entera

    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)  # FONDO BLANCO
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, FRANJA_AZUL_Y, fill=COLOR_AZUL)  # FRANJA SUPERIOR AZUL
    gamelib.draw_text('Equipo {} vs Equipo {}'.format(equipo_1[1], equipo_2[1]), MITAD_X, TITULO_Y, fill='white', size=30, anchor='s')  # TITULO
    gamelib.draw_text('Jugador 1', 10, ALTO_VENTANA - 10) #
    gamelib.draw_text('Jugador 2', 500, FRANJA_AZUL_Y) #
    gamelib.draw_image(info_combat_1[1], 10, 300 + 20) #
    gamelib.draw_image(info_combat_2[1], 500, FRANJA_AZUL_Y + 20) #
    gamelib.draw_rectangle(10,  300, (10 +  ANCHO_RECTANGULO_HP) * hp_pocentaje_1, 300 + 5) #
    gamelib.draw_rectangle(500, 300, (500 + ANCHO_RECTANGULO_HP) * hp_pocentaje_2, 300 + 5) #
    """
    for i in range (len(vivos_1)):
        gamelib.draw_image(i)
    for i in range (len(vivos_2)):
        gamelib.draw_image(i)
    """
    # Mostrar pokemones que todavía están vivos_1 ?
    # Mostrar pokemones que todavía están vivos_2 ?

    gamelib.draw_end()


def un_turno(combatiente1, combatiente2, equipo1, equipo2, vivos_1, vivos_2):
    """
    Desarrolla un turno. Llama a dibujar el estado actual del combate, luego permite a los usuarios elegir sus movimientos.
    Calcula quien mueve primero y luego llama a las funciones calculadoras de daño, efecto y sanacion.
    """
    dibujar_combate(combatiente1, combatiente2, equipo1, equipo2, vivos_1, vivos_2)
    movimiento_jug_1 = jugador_elige_movimiento(equipo1, (combatiente1.informacion())[0])
    movimiento_jug_2 = jugador_elige_movimiento(equipo2, (combatiente2.informacion())[0])
    mas_rapido = quien_primero(combatiente1, combatiente2)
    if mas_rapido == 1:
        # CALCULAR QUE HACE movimiento_jug_1
        if combatiente2.esta_vivo() == False:
            pass
    if mas_rapido == 2:
        # CALCULAR QUE HACE movimiento_jug_2
        if combatiente1.esta_vivo() == False:
            pass

    pass


def desarrollo_combate(equipo1, equipo2):
    """
    Recibe las dos listas de equipos que eligieron los usuarios en prebatalla.py
    y desarrolla el combate. Termina cuando uno de los dos equipos se queda sin pokemones vivos
    """
    vivos_1 = lectores.extraer_integrantes_equipo(equipo1)
    vivos_2 = lectores.extraer_integrantes_equipo(equipo2)
    eleccion1 = jugador_elige_pokemon(vivos_1)
    eleccion2 = jugador_elige_pokemon(vivos_2)
    #print ('150 |', eleccion1, eleccion2)
    #print ('151 |', equipo1, equipo2)
    combatiente1 = Combatiente(eleccion1, equipo1)
    combatiente2 = Combatiente(eleccion2, equipo2)

    while not len(equipo1) == 0 or not len(equipo2) == 0:
        un_turno(combatiente1, combatiente2, equipo1, equipo2, vivos_1, vivos_2)

        if combatiente1.esta_vivo() == False:
            informacion = combatiente1.informacion()
            equipo1.remove(informacion)  # STR
            combatiente1.reemplazar(jugador_elige_pokemon(equipo1), equipo1)

        elif combatiente2.esta_vivo() == False:
            informacion = combatiente2.informacion()
            equipo2.remove(informacion)  # STR
            combatiente2.reemplazar(jugador_elige_pokemon(equipo2), equipo2)

    if len(equipo1) == 0:
        gamelib.say('Felicidades, ganó el jugador 2!')

    elif len(equipo2) == 0:
        gamelib.say('Felicidades, ganó el jugador 1!')

# Prueba
