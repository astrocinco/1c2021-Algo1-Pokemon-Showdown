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
    def __init__(self, numero, lista):
        """Crea por primera vez un combatiente, recibiendo su número y sus movimientos disponibles."""
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
        self.movimientos = lectores.movimiento_en_pokemon(lista, numero)

    def esta_vivo(self):
        """Retorna True o False si el pokemón está vivo (si su salud está por encima de 0)."""
        if self.hp > 0:
            return True
        else: return False

    def reemplazar(self, numero, lista):
        """Reemplaza todas las stats según el número del nuevo pokemón."""
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
        self.movimientos = lectores.movimiento_en_pokemon(lista, numero)

    def limpiar_stat_boost(self):
        """
        Devuelve los atributos de ataque, defensa y velocidad 
        a los que están en pokemons.csv para limpiar cualquier stat boost que pudo haber sido aplicado.
        """
        stats = lectores.lector_por_numero(self.numero, ARCHIVO_POKEMONES)
        self.ataque = int(stats[5])
        self.defensa = int(stats[6])
        self.speat = int(stats[7])
        self.spedf = int(stats[8])
        self.velocidad = int(stats[9])

    def curar(self, nueva_hp):
        """Cambia la salud del pokemon por la ingresada."""
        self.hp = nueva_hp

    def herir(self, nueva_hp):
        """Cambia la salud del pokemon por la ingresada."""
        self.hp = nueva_hp

    def informacion(self):
        """Retorna todos los atributos del pokemon en juego."""
        return self.numero, self.imagen, self.nombre, self.tipos, self.hp, self.ataque, self.defensa, self.speat, self.spedf, self.velocidad, self.movimientos


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
        #print ('68 |', lista)
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
    opciones = lectores.movimiento_en_pokemon(lista, numero)

    while eleccion == '':
        ingreso = gamelib.input(MENSAJE_ELIJA_MOVIMIENTO.format(numero_a_nombre(numero), opciones))
        if ingreso == None:
            gamelib.say(MENSAJE_ERROR_ELECCION_MOVIMIENTO)
            continue
        if ingreso in opciones:
            eleccion = ingreso
        else: gamelib.say(MENSAJE_ERROR_ELECCION_MOVIMIENTO)
    #print ('97 |', eleccion)
    return eleccion


def calculadora_daño(movimiento, combatienteactua, combatientedefiende):
    """
    Hace todos los calculos de daño, retorna el numero de daño hecho.
    """
    info = combatientedefiende.informacion() 
    resultado = info[4] - 400 # DEBUG. REMPLAZAR EL 80 POR LO QUE HACE EL COMBATIENTE QUE ACTUA

    combatientedefiende.herir(resultado)


def calculadora_efecto(movimiento, combatienteactua, combatientedefiende):
    """
    Hace todos los calculos de stat boost, retorna los efectos.
    """
    pass


def calculadora_sanacion(combatienteactua):
    """
    Al ser llamada, calcula cuánto debe ser sanado un pokemon.
    """
    info = combatienteactua.informacion()
    max_hp_posible = int((lectores.lector_por_numero(int(info[0]), ARCHIVO_POKEMONES))[4]) + 110
    resultado = info[4] + max_hp_posible // 2
    if resultado > max_hp_posible:
        resultado = max_hp_posible

    combatienteactua.curar(resultado)


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


def calcular_movimiento(movimiento, combatienteactua, combatientedefiende):
    """
    Recibe el movimiento que se usará, y los dos objetos de los pokemones en juego
    y define a qué calculadora se debe llamar según si el movimiento es de tipo
    ataque, stat boost o sanación.
    """
    informacion = lectores.detalles_movimiento(movimiento, ARCHIVO_DETALLE_MOVIMIENTOS)
    #print ('142 | ', informacion)
    if informacion['categoria'] == 'Special' or  informacion['categoria'] == 'Physical':
        print ('Trigger daño')
        calculadora_daño(movimiento, combatienteactua, combatientedefiende)
    elif informacion['categoria'] == 'Status' and informacion['objetivo'] == 'self' and informacion['stats'] == '':
        print ('Trigger sanacion')
        calculadora_sanacion(combatienteactua)
    elif informacion['categoria'] == 'Status':
        print ('Trigger stat boost')
        calculadora_efecto(movimiento, combatienteactua, combatientedefiende)
    else:
        raise Exception('Error en calcular movimientos')


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
    #BARRA_HP_1_X = 

    info_combat_1 = combatiente1.informacion()
    info_combat_2 = combatiente2.informacion()
    #print ('154 | ', info_combat_1, info_combat_2)
    #print ('155 | ', info_combat_1[0])
    hp_combat_1_entera = int(lectores.lector_por_numero(info_combat_1[0], ARCHIVO_POKEMONES)[4]) + 110
    hp_combat_2_entera = int(lectores.lector_por_numero(info_combat_2[0], ARCHIVO_POKEMONES)[4]) + 110
    hp_combat_1_actual = info_combat_1[4]
    hp_combat_2_actual = info_combat_2[4]
    hp_pocentaje_1 = hp_combat_1_actual / hp_combat_1_entera
    hp_pocentaje_2 = hp_combat_2_actual / hp_combat_2_entera
    color_1 = 'green'
    color_2 = 'orange'
    print ('199 |', hp_pocentaje_1, hp_pocentaje_2)
    #hp_pocentaje_2 = 0.2 ###################### DEBUG

    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)  # FONDO BLANCO
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, FRANJA_AZUL_Y, fill=COLOR_AZUL)  # FRANJA SUPERIOR AZUL
    gamelib.draw_text('Equipo {} vs Equipo {}'.format(equipo_1[1], equipo_2[1]), MITAD_X, TITULO_Y, fill='white', size=30, anchor='s')  # TITULO
    gamelib.draw_text('Jugador 1', 10, ALTO_VENTANA - 10, fill='black', anchor='w') #
    gamelib.draw_text('Jugador 2', ANCHO_VENTANA, FRANJA_AZUL_Y, fill='black', anchor='ne') #
    gamelib.draw_image(info_combat_1[1], 10, 240) #
    gamelib.draw_image(info_combat_2[1], 500, FRANJA_AZUL_Y + 20) #
    gamelib.draw_rectangle(10,  200, 10 +  ANCHO_RECTANGULO_HP, 200 + 10, fill='black') # BARRA HP TOTAL 1
    gamelib.draw_rectangle(600, 450, 600 + ANCHO_RECTANGULO_HP, 450 + 10, fill='black') # BARRA HP TOTAL 2
    gamelib.draw_rectangle(10,  200, 10 +  ANCHO_RECTANGULO_HP * hp_pocentaje_1, 200 + 10, fill=color_1) # BARRA HP RESTANTE 1
    gamelib.draw_rectangle(600, 450, 600 + ANCHO_RECTANGULO_HP * hp_pocentaje_2, 450 + 10, fill=color_2) # BARRA HP RESTANTE 2
    """
    for i in range (len(vivos_1)):
        gamelib.draw_image(i)
    for i in range (len(vivos_2)):
        gamelib.draw_image(i)
    """

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
        calcular_movimiento(movimiento_jug_1, combatiente1, combatiente2)
        if not combatiente2.esta_vivo(): 
            print ('A')
            return
        calcular_movimiento(movimiento_jug_2, combatiente2, combatiente1)
    if mas_rapido == 2:
        calcular_movimiento(movimiento_jug_2, combatiente2, combatiente1)
        if not combatiente1.esta_vivo(): 
            print ('B')
            return 
        calcular_movimiento(movimiento_jug_1, combatiente1, combatiente2)


def desarrollo_combate(equipo1, equipo2):
    """
    Recibe las dos listas de equipos que eligieron los usuarios en prebatalla.py
    y desarrolla el combate. Termina cuando uno de los dos equipos se queda sin pokemones vivos
    """
    vivos_1 = lectores.extraer_integrantes_equipo(equipo1)
    vivos_2 = lectores.extraer_integrantes_equipo(equipo2)
    eleccion1 = jugador_elige_pokemon(vivos_1)
    eleccion2 = jugador_elige_pokemon(vivos_2)
    #print ('225 |', eleccion1, eleccion2)
    #print ('226 |', equipo1, equipo2)
    combatiente1 = Combatiente(eleccion1, equipo1)
    combatiente2 = Combatiente(eleccion2, equipo2)
    contador_turno = 0

    while not len(vivos_1) == 0 and not len(vivos_2) == 0:
        print ('263 |', len(vivos_1), len(vivos_2))
        un_turno(combatiente1, combatiente2, equipo1, equipo2, vivos_1, vivos_2)
        contador_turno += 1
        print ('266 |', contador_turno, combatiente1.informacion(), combatiente2.informacion())

        if not combatiente1.esta_vivo():
            informacion = combatiente1.informacion()
            print ('267 |', informacion, equipo1)
            vivos_1.remove(str(informacion[0]))
            equipo1.remove(str(informacion[0])) 
            if len(vivos_1) == 0:
                break
            combatiente1.reemplazar(jugador_elige_pokemon(vivos_1), equipo1)
            combatiente2.limpiar_stat_boost()

        elif not combatiente2.esta_vivo():
            informacion = combatiente2.informacion()
            print ('273 |', informacion, equipo2)
            vivos_2.remove(str(informacion[0]))
            equipo2.remove(str(informacion[0])) 
            if len(vivos_2) == 0:
                break
            combatiente2.reemplazar(jugador_elige_pokemon(vivos_2), equipo2)
            combatiente1.limpiar_stat_boost()

    print ('279 |', vivos_1, vivos_2)

    if len(vivos_1) == 0:
        gamelib.say('Felicidades, ganó el jugador 2!')

    elif len(vivos_2) == 0:
        gamelib.say('Felicidades, ganó el jugador 1!')
