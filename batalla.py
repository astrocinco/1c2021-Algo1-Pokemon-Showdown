import lectores
import gamelib
import random
import auxiliares

ANCHO_VENTANA = 900
ALTO_VENTANA = 600

ARCHIVO_POKEMONES = 'pokemons.csv'
ARCHIVO_DETALLE_MOVIMIENTOS = 'detalle_movimientos.csv'
ARCHIVO_TABLA_TIPOS = 'tabla_tipos.csv'

MENSAJE_ELIJA_PROX_COMBATIENTE = 'Ingrese el número del pokemon que luchará a continuación: {}'
MENSAJE_ERROR_ELECCION_PROX_COMBATIENTE = 'No eligió correctamente su pŕoximo combatiente. Inténtalo de nuevo'
MENSAJE_ELIJA_MOVIMIENTO = 'Elija que movimiento usará {} en este turno. Tienes disponibles: {}'
MENSAJE_ERROR_ELECCION_MOVIMIENTO = 'No eligió correctamente su pŕoximo movmiento. Inténtalo de nuevo'
MENSAJE_MUY_EFECTIVO = 'El ataque de {} a {} es muy efectivo!'
MENSAJE_POCO_EFECTIVO = 'El ataque de {} a {} es poco efectivo.'


class ClasePokemon:
    def __init__(self, par):
        """Crea al pokemon en juego, recibiendo su número y sus movimientos disponibles en una tupla.""" 
        stats = lectores.lector_por_numero(par[0], ARCHIVO_POKEMONES)
        lista_tipos = (stats['tipos']).split(',')
        
        self.numero = par[0]
        self.imagen = stats['imagen']
        self.nombre = stats['nombre']
        self.tipos = lista_tipos[0]
        self.hp = int(stats['hp']) + 110
        self.hpmax = int(stats['hp']) + 110
        self.ataque = int(stats['atk'])
        self.defensa = int(stats['def'])
        self.speat = int(stats['spa'])
        self.spedf = int(stats['spd'])
        self.velocidad = int(stats['spe'])
        self.movimientos = par[1]

    def __str__(self):
        """Retorna un string para imprimir el pokemon. Para uso de debugging exclusivamente"""
        return '{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}'.format(self.numero, self.imagen, self.nombre, self.tipos, self.hp, self.ataque, self.defensa, self.speat, self.spedf, self.velocidad, self.movimientos)

    def esta_vivo(self):
        """Retorna True o False si el pokemón está vivo (si su salud está por encima de 0)."""
        if self.hp > 0:
            return True
        else: return False

    def hacer_dano(self, defensor, movimiento):
        """
        Hace daño al pokemon que recibe el ataque.
        El moviento y el pokemon que recibe el ataque son ingresados por parámetro.
        """
        ataque = self.ataque
        defensa = defensor.defensa
        diccionario_efectividades = lectores.detalles_tipos(self.tipos, ARCHIVO_TABLA_TIPOS)
        roll = random.randint(80, 100)
        efectividad = float(diccionario_efectividades[defensor.tipos])

        if movimiento.categoria == 'Special':
            ataque = self.speat
            defensa = defensor.spedf

        if efectividad == 2:
            gamelib.say(MENSAJE_MUY_EFECTIVO.format(self.nombre, defensor.nombre))
        elif efectividad == 0.5:
            gamelib.say(MENSAJE_POCO_EFECTIVO.format(self.nombre, defensor.nombre))

        dano = 15 * movimiento.poder * (ataque / defensa) / 50

        if self.tipos == movimiento.tipo:
            dano *= 1.5

        defensor.hp -= int(dano * efectividad * (roll / 100))

    def stat_boost(self, ataque, defensa, speat, spedf, velocidad):
        """Boostea todos los atributos en los que recibe True"""
        if ataque:
            self.ataque = self.ataque * 2
        if defensa:
            self.defensa = self.defensa * 2
        if speat:
            self.speat = self.speat * 2
        if spedf:
            self.spedf = self.spedf * 2
        if velocidad:
            self.velocidad = self.velocidad * 2

    def stat_nerf(self, ataque, defensa, speat, spedf, velocidad): 
        """Nerfea todos los atributos en los que recibe True"""
        if ataque:
            self.ataque = self.ataque // 2
        if defensa:
            self.defensa = self.defensa // 2
        if speat:
            self.speat = self.speat // 2
        if spedf:
            self.spedf = self.spedf // 2
        if velocidad:
            self.velocidad = self.velocidad // 2

    def sanarse(self):
        """Al ser llamada, cura al pokemon."""
        self.hp += self.hpmax // 2
        if self.hp > self.hpmax:
            self.hp = self.hpmax

    def limpiar_stat_boost(self):
        """
        Devuelve los atributos de ataque, defensa y velocidad 
        a los que están en pokemons.csv para limpiar cualquier stat boost que pudo haber sido aplicado.
        """
        stats = lectores.lector_por_numero(self.numero, ARCHIVO_POKEMONES)
        self.ataque = int(stats['atk'])
        self.defensa = int(stats['def'])
        self.speat = int(stats['spa'])
        self.spedf = int(stats['spd'])
        self.velocidad = int(stats['spe'])


class ClaseMovimiento:
    def __init__(self, nombre_movimiento):
        diccionario_info = lectores.lector_por_nombre(nombre_movimiento, ARCHIVO_DETALLE_MOVIMIENTOS)
        self.no_modelado = False
        if diccionario_info == None:
            self.no_modelado = True
            return
        self.nombre = diccionario_info['nombre']
        self.categoria = diccionario_info['categoria']
        self.objetivo = diccionario_info['objetivo']
        self.poder = int(diccionario_info['poder'])
        self.tipo = diccionario_info['tipo']
        self.stats = diccionario_info['stats'].split(';')

    def __str__(self):
        return '{}-{}-{}-{}-{}-{}'.format(self.nombre, self.categoria, self.objetivo, self.poder, self.tipo, self.stats)


def numero_a_nombre(nro):
    """
    Recibe el número de un pokemon y retorna su nombre en string.
    """
    info = lectores.lector_por_numero(nro, ARCHIVO_POKEMONES)

    return info['nombre']


def jugador_elige_pokemon(equipo):
    """
    Recibe una lista de pokemones de todo el equipo que puede elegir el usuario
    y retorna el que elija el usuario.
    """
    lista_en_nombres = []
    for par in equipo.pokmov:
        lista_en_nombres.append((numero_a_nombre(par[0]), par[0]))

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


def elegir_boost_o_nerf(movimiento, combatienteactua, combatientedefiende):
    """
    Hace todos los calculos de stat boost, retorna los efectos.
    """
    if movimiento.objetivo == 'self':
        for elemento in movimiento.stats:
            if elemento == 'atk':
                combatienteactua.stat_boost(True, False, False, False, False)
            if elemento == 'def':
                combatienteactua.stat_boost(False, True, False, False, False)
            if elemento == 'speat':
                combatienteactua.stat_boost(False, False, True, False, False) 
            if elemento == 'spedf':
                combatienteactua.stat_boost(False, False, False, True, False) 
            if elemento == 'spe':
                combatienteactua.stat_boost(False, False, False, False, True)

    if movimiento.objetivo == 'normal':
        for elemento in movimiento.stats:
            if elemento == 'atk':
                combatientedefiende.stat_nerf(True, False, False, False, False)
            if elemento == 'def':
                combatientedefiende.stat_nerf(False, True, False, False, False)
            if elemento == 'speat':
                combatientedefiende.stat_nerf(False, False, True, False, False)  
            if elemento == 'spedf':
                combatientedefiende.stat_nerf(False, False, False, True, False) 
            if elemento == 'spe':
                combatientedefiende.stat_nerf(False, False, False, False, True)


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


def calcular_movimiento(movimiento, combatienteactua, combatientedefiende):
    """
    Recibe el movimiento que se usará, y los dos objetos de los pokemones en juego
    y define a qué calculadora se debe llamar según si el movimiento es de tipo
    ataque, stat boost o sanación.
    """
    if movimiento.categoria == 'Special' or  movimiento.categoria == 'Physical':
        combatienteactua.hacer_dano(combatientedefiende, movimiento)

    elif movimiento.categoria == 'Status' and movimiento.objetivo == 'self' and movimiento.stats == '':
        combatienteactua.sanarse() 

    elif movimiento.categoria == 'Status':
        elegir_boost_o_nerf(movimiento, combatienteactua, combatientedefiende)

    else:
        raise Exception('Error en calcular el tipo de movimiento.')


def dibujar_combate(combatiente1, combatiente2, equipo_1, equipo_2): 
    """
    Dibuja el estado del combate al principio del turno, para que los usuarios puedan elegir que hacer a continuación según
    cómo ven que están sus pokemones en juego.
    """
    VACIO = 0
    FRANJA_AZUL_Y = 88
    TITULO_Y = 70
    COLOR_AZUL = '#0d1364'
    MITAD_X = ANCHO_VENTANA // 2
    ANCHO_RECTANGULO_HP = 300
    J1_X = 10
    J1_Y = 200
    J2_X = 550
    J2_Y = 450
    ALTO_BARRA_HP = 10
    INICIO_ESFERAS_1 = 550
    INICIO_ESFERAS_2 = 210

    hp_pocentaje_1 = combatiente1.hp / combatiente1.hpmax
    hp_pocentaje_2 = combatiente2.hp / combatiente2.hpmax
    if hp_pocentaje_1 < 0.0:
        hp_pocentaje_1 = 0.0
    if hp_pocentaje_2 < 0.0:
        hp_pocentaje_2 = 0.0
    color_1 = auxiliares.color_barra(hp_pocentaje_1)
    color_2 = auxiliares.color_barra(hp_pocentaje_2)
    TEXTO_MOSTRAR_STATS = '{} {}, Tipo: {}, HP: {}, Ataque: {}, Defensa: {}, S-Ataque:{}, S-Defensa: {}, Velocidad: {}'
    TEXTO_MOSTRAR_STATS_1 = TEXTO_MOSTRAR_STATS.format(combatiente1.nombre, combatiente1.numero, combatiente1.tipos, combatiente1.hp, combatiente1.ataque, combatiente1.defensa, combatiente1.speat, combatiente1.spedf, combatiente1.velocidad)
    TEXTO_MOSTRAR_STATS_2 = TEXTO_MOSTRAR_STATS.format(combatiente2.nombre, combatiente2.numero, combatiente2.tipos, combatiente2.hp, combatiente2.ataque, combatiente2.defensa, combatiente2.speat, combatiente2.spedf, combatiente2.velocidad)

    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA + 10, ALTO_VENTANA + 10)  # FONDO BLANCO
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, FRANJA_AZUL_Y, fill=COLOR_AZUL)  # FRANJA SUPERIOR AZUL
    gamelib.draw_text('Equipo {} vs Equipo {}'.format(equipo_1.nombre, equipo_2.nombre), MITAD_X, TITULO_Y, fill='white', size=30, anchor='s')  # TITULO
    gamelib.draw_text('Jugador 1', 10, ALTO_VENTANA - 10, fill='red', anchor='w')  # TEXTO ESQUINA PARA CADA JUGADOR
    gamelib.draw_text('Jugador 2', ANCHO_VENTANA, FRANJA_AZUL_Y + 5, fill=COLOR_AZUL, anchor='ne')  # TEXTO ESQUINA PARA CADA JUGADOR
    gamelib.draw_text(TEXTO_MOSTRAR_STATS_1, 100, ALTO_VENTANA - 10, fill='red', anchor='w')  # TEXTO STATS J1
    gamelib.draw_text(TEXTO_MOSTRAR_STATS_2, ANCHO_VENTANA - 100, FRANJA_AZUL_Y + 5, fill=COLOR_AZUL, anchor='ne')  # TEXTO STATS J2
    gamelib.draw_text('HP: {}'.format(combatiente1.hp), J1_X, J1_Y - 20, fill='black', anchor='w')  # TEXTO NUMERO HP J1
    gamelib.draw_text('HP: {}'.format(combatiente2.hp), J2_X, J2_Y + 20, fill='black', anchor='nw')  # TEXTO NUMERO HP J2
    gamelib.draw_image(combatiente1.imagen, 0, J1_Y + 40)  # IMAGEN POKEMON J1
    gamelib.draw_image(combatiente2.imagen, J2_X - 70, FRANJA_AZUL_Y + 40)  # IMAGEN POKEMON J2
    gamelib.draw_rectangle(J1_X,  J1_Y, J1_X +  ANCHO_RECTANGULO_HP, J1_Y + ALTO_BARRA_HP, fill='black') # BARRA HP TOTAL 1
    gamelib.draw_rectangle(J2_X, J2_Y, J2_X + ANCHO_RECTANGULO_HP, J2_Y + ALTO_BARRA_HP, fill='black') # BARRA HP TOTAL 2
    gamelib.draw_rectangle(J1_X,  J1_Y, J1_X +  ANCHO_RECTANGULO_HP * hp_pocentaje_1, J1_Y + ALTO_BARRA_HP, fill=color_1) # BARRA HP RESTANTE 1
    gamelib.draw_rectangle(J2_X, J2_Y, J2_X + ANCHO_RECTANGULO_HP * hp_pocentaje_2, J2_Y + ALTO_BARRA_HP, fill=color_2) # BARRA HP RESTANTE 2

    contador_color_1 = 0
    for i in range (6):  # PUNTOS DE COLOR QUE INDICAN LOS POKEMONES VIVOS RESTANTES
        if contador_color_1 < len(equipo_1.pokmov):
            color_vivos = 'green'
        if contador_color_1 >= len(equipo_1.pokmov):
            color_vivos = 'red'
        gamelib.draw_oval(10, INICIO_ESFERAS_1 - (15 * i), 20, INICIO_ESFERAS_1 + 10 - (15 * i), fill=color_vivos)
        contador_color_1 += 1

    contador_color_2 = 0
    for i in range (6):  # PUNTOS DE COLOR QUE INDICAN LOS POKEMONES VIVOS RESTANTES
        if contador_color_2 < len(equipo_2.pokmov):
            color_vivos = 'green'
        if contador_color_2 >= len(equipo_2.pokmov):
            color_vivos = 'red'
        gamelib.draw_oval(ANCHO_VENTANA - 20, INICIO_ESFERAS_2 - (15 * i), ANCHO_VENTANA - 10, INICIO_ESFERAS_2 + 10 - (15 * i), fill=color_vivos)
        contador_color_2 += 1

    gamelib.draw_end()


def un_turno(combatiente1, combatiente2, equipo1, equipo2): 
    """
    Desarrolla un turno. Llama a dibujar el estado actual del combate, luego permite a los usuarios elegir sus movimientos.
    Calcula quien mueve primero y luego llama a las funciones calculadoras de daño, efecto y sanacion.
    """
    dibujar_combate(combatiente1, combatiente2, equipo1, equipo2) 
    movimiento_jug_1 = ClaseMovimiento(jugador_elige_movimiento(combatiente1))
    movimiento_jug_2 = ClaseMovimiento(jugador_elige_movimiento(combatiente2))
    mas_rapido = quien_primero(combatiente1, combatiente2)

    if movimiento_jug_1.no_modelado or movimiento_jug_2.no_modelado:
        gamelib.say('Uno de los movimientos elegidos no está modelado en el juego.')
        return 

    if mas_rapido == 1:
        calcular_movimiento(movimiento_jug_1, combatiente1, combatiente2)
        if not combatiente2.esta_vivo(): 
            dibujar_combate(combatiente1, combatiente2, equipo1, equipo2)
            return
        calcular_movimiento(movimiento_jug_2, combatiente2, combatiente1)

    if mas_rapido == 2:
        calcular_movimiento(movimiento_jug_2, combatiente2, combatiente1)
        if not combatiente1.esta_vivo(): 
            dibujar_combate(combatiente1, combatiente2, equipo1, equipo2)
            return 
        calcular_movimiento(movimiento_jug_1, combatiente1, combatiente2)


def desarrollo_combate(equipo1, equipo2):
    """
    Recibe las dos listas de equipos que eligieron los usuarios en prebatalla.py
    y desarrolla el combate. Termina cuando uno de los dos equipos se queda sin pokemones vivos
    """
    combatiente1 = ClasePokemon(jugador_elige_pokemon(equipo1)) 
    combatiente2 = ClasePokemon(jugador_elige_pokemon(equipo2))

    while not len(equipo1.pokmov) == 0 and not len(equipo2.pokmov) == 0:
        un_turno(combatiente1, combatiente2, equipo1, equipo2)

        if not combatiente1.esta_vivo():
            equipo1.eliminar_pokemon_derrotado(combatiente1)
            if len(equipo1.pokmov) == 0:
                break

            combatiente1 = ClasePokemon(jugador_elige_pokemon(equipo1))
            combatiente2.limpiar_stat_boost()

        elif not combatiente2.esta_vivo():
            equipo2.eliminar_pokemon_derrotado(combatiente2)
            if len(equipo2.pokmov) == 0:
                break

            combatiente2 = ClasePokemon(jugador_elige_pokemon(equipo2))
            combatiente1.limpiar_stat_boost()

    if len(equipo1.pokmov) == 0:
        gamelib.say('Felicidades, ganó el jugador 2!')

    elif len(equipo2.pokmov) == 0:
        gamelib.say('Felicidades, ganó el jugador 1!')

    return 
