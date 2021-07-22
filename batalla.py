import lectores
import gamelib

archivo_pokemones = 'pokemons.csv'

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


def un_turno(combatiente1, combatiente2, equipo1, equipo2):
    #draw estado actual del juego
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