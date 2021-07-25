import lectores
import gamelib

ANCHO_VENTANA = 900
ALTO_VENTANA = 600

archivo_pokemones = 'pokemons.csv'
archivo_detalle_movimientos = 'detalle_movimientos.csv'
archivo_tabla_tipos = 'tabla_tipos.csv'

MENSAJE_ELIJA_PROX_COMBATIENTE = 'Ingrese el número del pokemon que luchará a continuación: {}'
MENSAJE_ERROR_ELECCION_PROX_COMBATIENTE = 'No eligió correctamente su pŕoximo combatiente. Inténtalo de nuevo'

class Combatiente:
    def __init__(self, numero, archivo):
        stats = lectores.lector_por_numero(numero, archivo_pokemones)
        self.numero = int(stats[0])
        self.imagen = stats[1]
        self.nombre = stats[2]
        self.tipos = stats[3]
        self.hp = int(stats[4])
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
        stats = lectores.lector_por_numero(numero, archivo_pokemones)
        self.numero = stats[0]
        self.imagen = stats[1]
        self.nombre = stats[2]
        self.tipos = stats[3]
        self.hp = stats[4]
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
    info = lectores.lector_por_numero(nro, archivo_pokemones)
    print ('57 |', info)
    return info[2]


def jugador_elige_pokemon(lista):
    """
    Recibe una lista de pokemones de todo el equipo que puede elegir el usuario
    y retorna el que elija el usuario.
    """
    lista_en_nombres = []
    for i in range (len(lista)):
        print ('68 |', lista[i])
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
    return 'fly' # HACER


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


def dibujar_combate(nombre_1, nombre_2):
    """
    Dibuja el estado del combate al principio del turno, para que los usuarios puedan elegir que hacer a continuación según
    cómo ven que están sus pokemones en juego.
    """
    VACIO = 0
    FRANJA_AZUL_Y = 88
    TITULO_Y = 70
    COLOR_AZUL = '#0d1364'
    MITAD_X = ANCHO_VENTANA // 2
    print ('120 | ', nombre_1, nombre_2)
    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)  # FONDO BLANCO
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, FRANJA_AZUL_Y, fill=COLOR_AZUL)  # FRANJA SUPERIOR AZUL
    gamelib.draw_text('Equipo {} vs Equipo {}'.format(nombre_1[1], nombre_2[1]), MITAD_X, TITULO_Y, fill='white', size=30, anchor='s')  # TITULO
    #  SEGUIR
    gamelib.draw_end()


def un_turno(combatiente1, combatiente2, equipo1, equipo2):
    """
    Desarrolla un turno. Llama a dibujar el estado actual del combate, luego permite a los usuarios elegir sus movimientos.
    Calcula quien mueve primero y luego llama a las funciones calculadoras de daño, efecto y sanacion.
    """
    dibujar_combate(equipo1, equipo2)
    #movimiento_jug_1 = jugador_elige_movimiento(equipo1, combatiente1.informacion[0])
    #movimiento_jug_2 = jugador_elige_movimiento(equipo2, combatiente2.informacion[0])
    # SEGUIR. 
    # Quien mueve primero? Calcular efecto movimiento del primero. Afectar al otro. Calcular efecto segundo movimiento. Afectar al primero.

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
    print ('150 |', eleccion1, eleccion2)
    combatiente1 = Combatiente(eleccion1, equipo1)
    combatiente2 = Combatiente(eleccion2, equipo2)

    while not len(equipo1) == 0 or not len(equipo2) == 0:
        un_turno(combatiente1, combatiente2, equipo1, equipo2) 

        if combatiente1.esta_vivo() == False:
            informacion = combatiente1.informacion()
            equipo1.remove(informacion)
            combatiente1.reemplazar(jugador_elige_pokemon(equipo1), equipo1)

        elif combatiente2.esta_vivo() == False:
            informacion = combatiente2.informacion()
            equipo2.remove(informacion)
            combatiente2.reemplazar(jugador_elige_pokemon(equipo2), equipo2)

    if len(equipo1) == 0:
        gamelib.say('Felicidades, ganó el jugador 2!')

    elif len(equipo2) == 0:
        gamelib.say('Felicidades, ganó el jugador 1!')
