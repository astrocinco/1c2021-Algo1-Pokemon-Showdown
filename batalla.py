import lectores
import gamelib
ANCHO_VENTANA = 900
ALTO_VENTANA = 600

archivo_pokemones = 'pokemons.csv'
print ('7')
class Combatiente:
    def __init__(self, numero, archivo):
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


def jugador_elige_pokemon(lista):
    """
    Recibe una lista de todo el equipo que puede elegir el usuario
    y retorna uno de ellos
    """
    return 1 # HACER


def jugador_elige_movimiento(lista, numero):
    """
    Recibe una lista de todo el equipo y un numero de pokemon
    y retorna el movimiento que elegió el usuario para ese pokemon
    """
    return 1 # HACER


def calculadora_daño():
    pass


def calculadora_efecto():
    pass


def calculadora_sanacion():
    pass


def dibujar_combate():
    VACIO = 0
    FRANJA_AZUL_Y = 88
    TITULO_Y = 70
    COLOR_AZUL = '#0d1364'
    MITAD_X = ANCHO_VENTANA // 2
    nombre_1 = 'Rocket'
    nombre_2 = 'Ash'
    print ('Hola')

    while gamelib.is_alive(): # probablemente esté mal hacer una instancia nueva de gamelib acá. Despues lo estudiamos
        ev = gamelib.wait()

        if not ev:
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':      
            break

        gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

        gamelib.draw_begin()
        gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)  # FONDO BLANCO
        gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, FRANJA_AZUL_Y, fill=COLOR_AZUL)  # FRANJA SUPERIOR AZUL
        #gamelib.draw_rectangle(VACIO, ALTO_VENTANA - FRANJA_AZUL_Y, ANCHO_VENTANA, ALTO_VENTANA, fill=COLOR_AZUL)  # FRANJA INFERIOR AZUL
        gamelib.draw_text('Equipo {} vs Equipo {}'.format(nombre_1, nombre_2), MITAD_X, TITULO_Y, fill='white', size=30, anchor='s')  # TITULO
        gamelib.draw_end()


def un_turno(combatiente1, combatiente2, equipo1, equipo2):
    print ('si')
    gamelib.init(dibujar_combate) 
    movimiento_jug_1 = jugador_elige_movimiento(equipo1, combatiente1.informacion[0])
    movimiento_jug_2 = jugador_elige_movimiento(equipo2, combatiente2.informacion[0])

    # HACER. Quien mueve primero? Calcular efecto movimiento del primero. Afectar al otro. Calcular efecto segundo movimiento. Afectar al primero.

    #draw como quedaron despues del combate (van a tener menos hp o se va a ver como uno murió)


def desarrollo_combate(equipo1, equipo2):
    """
    Recibe las dos listas de equipos que eligieron los usuarios en prebatalla.py
    y desarrolla el combate. Termina cuando uno de los dos equipos se queda sin pokemones vivos
    """
    eleccion1 = jugador_elige_pokemon(equipo1)
    eleccion2 = jugador_elige_pokemon(equipo2)
    combatiente1 = Combatiente(eleccion1, equipo1)
    combatiente2 = Combatiente(eleccion2, equipo2)

    while not len(equipo1) == 0 or not len(equipo2) == 0:
        un_turno(combatiente1, combatiente2, equipo1, equipo2) 

        if combatiente1.esta_vivo() == False:
            #equipo1.remove(combatiente1.informacion[0])
            combatiente1.reemplazar(jugador_elige_pokemon(equipo1), equipo1)

        elif combatiente2.esta_vivo() == False:
            #equipo2.remove(combatiente2.informacion[0])
            combatiente2.reemplazar(jugador_elige_pokemon(equipo2), equipo2)

    if len(equipo1) == 0:
        gamelib.say('Felicidades, ganó el jugador 2!')

    elif len(equipo2) == 0:
        gamelib.say('Felicidades, ganó el jugador 1!')

print('129')
un_turno('', '', '', '')
