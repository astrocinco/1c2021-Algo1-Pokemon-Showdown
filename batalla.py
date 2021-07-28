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

    def stat_boost(self, ataque, defensa, speat, spedf, velocidad):
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

    return info[2]


def jugador_elige_pokemon(lista):
    """
    Recibe una lista de pokemones de todo el equipo que puede elegir el usuario
    y retorna el que elija el usuario.
    """
    lista_en_nombres = []
    for i in range (len(lista)):
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

    return eleccion


def calculadora_daño(movimiento, combatienteactua, combatientedefiende):
    """
    Hace todos los calculos de daño, retorna el numero de daño hecho.
    """
    info_defensor = combatientedefiende.informacion()
    info_atacante = combatienteactua.informacion()
    tipo_atacante = info_atacante[3]
    tipo_defensor = info_defensor[3]
    poder_base_del_ataque = lectores.detalles_movimiento(movimiento, ARCHIVO_DETALLE_MOVIMIENTOS)["poder"]
    ataque_simple= info_atacante[5]
    SpAtaque_atacante = info_atacante[7]
    defensa_simple = info_defensor[6]
    spdefensa_defensor = info_defensor[8]
    special_or_not_atk = {}
    special_or_not_dfe = {}
    special_or_not_atk["damage"] = ataque_simple
    special_or_not_dfe["defensa"] = defensa_simple
    stab = {"multiplicador": 1}
    type_movement = lectores.detalles_movimiento(movimiento, ARCHIVO_DETALLE_MOVIMIENTOS)["categoria"]
    efectividad_values = lectores.detalles_tipos(tipo_atacante, ARCHIVO_TABLA_TIPOS)
    efectividad = int(efectividad_values[tipo_defensor])
   
    if type_movement == "Special":
        special_or_not_atk["damage"] = SpAtaque_atacante
        special_or_not_dfe["defensa"] = spdefensa_defensor
    elif type_movement == "Physical":
        special_or_not_atk["damage"] = ataque_simple
        special_or_not_dfe["defensa"] = defensa_simple
   
    if type_movement == tipo_atacante:
        stab["multiplicador": 1.5]

    
    base_damage = 15 * poder_base_del_ataque * (special_or_not_atk["damage"] / special_or_not_dfe["defensa"] / 50)
    damage = base_damage * stab["multiplicador"] * efectividad
    resultado = info_defensor[4] - damage

    combatientedefiende.herir(resultado)


def calculadora_efecto(movimiento, combatienteactua, combatientedefiende):
    """
    Hace todos los calculos de stat boost, retorna los efectos.
    """
    info_movimiento = lectores.detalles_movimiento(movimiento, ARCHIVO_DETALLE_MOVIMIENTOS)
    stats_afectadas = info_movimiento['stats'].split(';')

    if info_movimiento['objetivo'] == 'self':
        for elemento in stats_afectadas:
            if elemento == 'atk':
                combatienteactua.stat_boost(True, False, False, False, False)
            if elemento == 'def':
                combatienteactua.stat_boost(False, True, False, False, False)
            if elemento == 'speat':
                combatienteactua.stat_boost(False, False, True, False, False)  # Los stat_boost de Special Attack  no existen, pero si se quisiese implementar es posible con estas lineas
            if elemento == 'spedf':
                combatienteactua.stat_boost(False, False, False, True, False)  # Los stat_boost de Special Defense no existen, pero si se quisiese implementar es posible con estas lineas
            if elemento == 'spe':
                combatienteactua.stat_boost(False, False, False, False, True)

    if info_movimiento['objetivo'] == 'normal':
        for elemento in stats_afectadas:
            if elemento == 'atk':
                combatientedefiende.stat_nerf(True, False, False, False, False)
            if elemento == 'def':
                combatientedefiende.stat_nerf(False, True, False, False, False)
            if elemento == 'speat':
                combatientedefiende.stat_nerf(False, False, True, False, False)  # Los stat_nerf de Special Attack  no existen, pero si se quisiese implementar es posible con estas lineas
            if elemento == 'spedf':
                combatientedefiende.stat_nerf(False, False, False, True, False)  # Los stat_nerf de Special Defense no existen, pero si se quisiese implementar es posible con estas lineas
            if elemento == 'spe':
                combatientedefiende.stat_nerf(False, False, False, False, True)


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
        aleatorio = random.choice(1, 2)
        return aleatorio
    else: raise Exception ('Error en función quien_primero()')


def calcular_movimiento(movimiento, combatienteactua, combatientedefiende):
    """
    Recibe el movimiento que se usará, y los dos objetos de los pokemones en juego
    y define a qué calculadora se debe llamar según si el movimiento es de tipo
    ataque, stat boost o sanación.
    """
    informacion = lectores.detalles_movimiento(movimiento, ARCHIVO_DETALLE_MOVIMIENTOS)
    if informacion['categoria'] == 'Special' or  informacion['categoria'] == 'Physical':
        calculadora_daño(movimiento, combatienteactua, combatientedefiende)

    elif informacion['categoria'] == 'Status' and informacion['objetivo'] == 'self' and informacion['stats'] == '':
        calculadora_sanacion(combatienteactua)

    elif informacion['categoria'] == 'Status':
        calculadora_efecto(movimiento, combatienteactua, combatientedefiende)

    else:
        raise Exception('Error en calcular movimientos')


def color_barra(porcentaje):
    if porcentaje >= 0.8:
        color = 'green'

    if 0.3 < porcentaje < 0.8:
        color = 'orange'
        
    if porcentaje <= 0.3:
        color = 'red'
    
    return color


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
    ANCHO_RECTANGULO_HP = 300
    J1_X = 10
    J1_Y = 200
    J2_X = 550
    J2_Y = 450
    ALTO_BARRA_HP = 10
    INICIO_ESFERAS_1 = 550
    INICIO_ESFERAS_2 = 210

    info_combat_1 = combatiente1.informacion()
    info_combat_2 = combatiente2.informacion()
    hp_combat_1_entera = int(lectores.lector_por_numero(info_combat_1[0], ARCHIVO_POKEMONES)[4]) + 110
    hp_combat_2_entera = int(lectores.lector_por_numero(info_combat_2[0], ARCHIVO_POKEMONES)[4]) + 110
    hp_combat_1_actual = info_combat_1[4]
    hp_combat_2_actual = info_combat_2[4]
    hp_pocentaje_1 = hp_combat_1_actual / hp_combat_1_entera
    hp_pocentaje_2 = hp_combat_2_actual / hp_combat_2_entera
    if hp_pocentaje_1 < 0.0:
        hp_pocentaje_1 = 0.0
    if hp_pocentaje_2 < 0.0:
        hp_pocentaje_2 = 0.0
    color_1 = color_barra(hp_pocentaje_1)
    color_2 = color_barra(hp_pocentaje_2)
    TEXTO_MOSTRAR_STATS = '{} {}, Tipo: {}, HP: {}, Ataque: {}, Defensa: {}, S-Ataque:{}, S-Defensa: {}, Velocidad: {}'
    TEXTO_MOSTRAR_STATS_1 = TEXTO_MOSTRAR_STATS.format(info_combat_1[2], info_combat_1[0], info_combat_1[3], info_combat_1[4], info_combat_1[5], info_combat_1[6], info_combat_1[7], info_combat_1[8], info_combat_1[9])
    TEXTO_MOSTRAR_STATS_2 = TEXTO_MOSTRAR_STATS.format(info_combat_2[2], info_combat_2[0], info_combat_2[3], info_combat_2[4], info_combat_2[5], info_combat_2[6], info_combat_2[7], info_combat_2[8], info_combat_2[9])

    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA + 10, ALTO_VENTANA + 10)  # FONDO BLANCO
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, FRANJA_AZUL_Y, fill=COLOR_AZUL)  # FRANJA SUPERIOR AZUL
    gamelib.draw_text('Equipo {} vs Equipo {}'.format(equipo_1[1], equipo_2[1]), MITAD_X, TITULO_Y, fill='white', size=30, anchor='s')  # TITULO
    gamelib.draw_text('Jugador 1', 10, ALTO_VENTANA - 10, fill='red', anchor='w')  # TEXTO ESQUINA PARA CADA JUGADOR
    gamelib.draw_text('Jugador 2', ANCHO_VENTANA, FRANJA_AZUL_Y + 5, fill=COLOR_AZUL, anchor='ne')  # TEXTO ESQUINA PARA CADA JUGADOR
    gamelib.draw_text(TEXTO_MOSTRAR_STATS_1, 100, ALTO_VENTANA - 10, fill='red', anchor='w')  # TEXTO STATS J1
    gamelib.draw_text(TEXTO_MOSTRAR_STATS_2, ANCHO_VENTANA - 100, FRANJA_AZUL_Y + 5, fill=COLOR_AZUL, anchor='ne')  # TEXTO STATS J2
    gamelib.draw_text('HP: {}'.format(hp_combat_1_actual), J1_X, J1_Y - 20, fill='black', anchor='w')  # TEXTO NUMERO HP J1
    gamelib.draw_text('HP: {}'.format(hp_combat_2_actual), J2_X, J2_Y + 20, fill='black', anchor='nw')  # TEXTO NUMERO HP J2
    gamelib.draw_image(info_combat_1[1], 0, J1_Y + 40)  # IMAGEN POKEMON J1
    gamelib.draw_image(info_combat_2[1], J2_X - 70, FRANJA_AZUL_Y + 40)  # IMAGEN POKEMON J2
    gamelib.draw_rectangle(J1_X,  J1_Y, J1_X +  ANCHO_RECTANGULO_HP, J1_Y + ALTO_BARRA_HP, fill='black') # BARRA HP TOTAL 1
    gamelib.draw_rectangle(J2_X, J2_Y, J2_X + ANCHO_RECTANGULO_HP, J2_Y + ALTO_BARRA_HP, fill='black') # BARRA HP TOTAL 2
    gamelib.draw_rectangle(J1_X,  J1_Y, J1_X +  ANCHO_RECTANGULO_HP * hp_pocentaje_1, J1_Y + ALTO_BARRA_HP, fill=color_1) # BARRA HP RESTANTE 1
    gamelib.draw_rectangle(J2_X, J2_Y, J2_X + ANCHO_RECTANGULO_HP * hp_pocentaje_2, J2_Y + ALTO_BARRA_HP, fill=color_2) # BARRA HP RESTANTE 2

    contador_color_1 = 0
    for i in range (6):  # PUNTOS DE COLOR QUE INDICAN LOS POKEMONES VIVOS RESTANTES
        if contador_color_1 < len(vivos_1):
            color_vivos = 'green'
        if contador_color_1 >= len(vivos_1):
            color_vivos = 'red'
        print (contador_color_1, len(vivos_1), color_vivos)
        gamelib.draw_oval(10, INICIO_ESFERAS_1 - (15 * i), 20, INICIO_ESFERAS_1 + 10 - (15 * i), fill=color_vivos)
        contador_color_1 += 1

    contador_color_2 = 0
    for i in range (6):  # PUNTOS DE COLOR QUE INDICAN LOS POKEMONES VIVOS RESTANTES
        if contador_color_2 < len(vivos_2):
            color_vivos = 'green'
        if contador_color_2 >= len(vivos_2):
            color_vivos = 'red'
        print (contador_color_2, len(vivos_2), color_vivos)
        gamelib.draw_oval(ANCHO_VENTANA - 20, INICIO_ESFERAS_2 - (15 * i), ANCHO_VENTANA - 10, INICIO_ESFERAS_2 + 10 - (15 * i), fill=color_vivos)
        contador_color_2 += 1

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
            dibujar_combate(combatiente1, combatiente2, equipo1, equipo2, vivos_1, vivos_2)
            return
        calcular_movimiento(movimiento_jug_2, combatiente2, combatiente1)
    if mas_rapido == 2:
        calcular_movimiento(movimiento_jug_2, combatiente2, combatiente1)
        if not combatiente1.esta_vivo(): 
            dibujar_combate(combatiente1, combatiente2, equipo1, equipo2, vivos_1, vivos_2)
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
    combatiente1 = Combatiente(eleccion1, equipo1)
    combatiente2 = Combatiente(eleccion2, equipo2)
    contador_turno = 0

    while not len(vivos_1) == 0 and not len(vivos_2) == 0:
        un_turno(combatiente1, combatiente2, equipo1, equipo2, vivos_1, vivos_2)
        contador_turno += 1

        if not combatiente1.esta_vivo():
            informacion = combatiente1.informacion()
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

    if len(vivos_1) == 0:
        gamelib.say('Felicidades, ganó el jugador 2!')

    elif len(vivos_2) == 0:
        gamelib.say('Felicidades, ganó el jugador 1!')
