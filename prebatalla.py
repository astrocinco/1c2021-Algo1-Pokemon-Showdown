import gamelib
import batalla
import lectores
import os

ANCHO_VENTANA = batalla.ANCHO_VENTANA
ALTO_VENTANA = batalla.ALTO_VENTANA

MENSAJE_INGRESE_RUTA = "Ingrese el nombre o la ruta en la que tiene sus equipos"
MENSAJE_ERROR_RUTA = "No se encontró un archivo con ese nombre o ruta"
MENSAJE_INGRESE_NRO_EQUIPO = "Ingrese el numero de equipo con el que va a jugar"
MENSAJE_ERROR_NRO = "No ingreso un numero. Ingrese el numero de equipo con el que va a jugar"
MENSAJE_ERROR_EQUIPO_INVALIDO = "No ingreso un equipo valido"
MENSAJE_ERROR_NECESITO_ARCHIVO= 'Debes elegir un archivo antes de elegir un equipo'
MENSAJE_FALTA_EQUIPO = 'No se eligieron dos equipos aún.'

MITAD_X = ANCHO_VENTANA // 2
MITAD_Y = ALTO_VENTANA // 2
VACIO = 0
FRANJA_AZUL_Y = 88
COLOR_AZUL = '#0d1364'
TITULO_Y = 70
BOTON_X = 120
BOTON_Y = 25
BOTON_ARCHIVOS_Y = 150
BOTON_EQUIPOS_Y = 350
TEXTO_ARCHIVOS_Y = 250
TEXTO_EQUIPOS_Y = 450
BOTON_FIN_ARCHIVOS_Y = ALTO_VENTANA - FRANJA_AZUL_Y // 2
BOTON_PRIMERMENU_X1, BOTON_PRIMERMENU_Y1, BOTON_PRIMERMENU_X2, BOTON_PRIMERMENU_Y2 = MITAD_X - BOTON_X, MITAD_Y - BOTON_Y, MITAD_X + BOTON_X, MITAD_Y + BOTON_Y #POSICION BOTON CENTRAL PRIMER MENU
BOTON_ARCHIVO1_X1, BOTON_ARCHIVO1_Y1, BOTON_ARCHIVO1_X2, BOTON_ARCHIVO1_Y2 = ANCHO_VENTANA // 4 - BOTON_X, BOTON_ARCHIVOS_Y - BOTON_Y, ANCHO_VENTANA // 4 + BOTON_X, BOTON_ARCHIVOS_Y + BOTON_Y #BOTON SELECCION ARCHIVO JUGADOR 1
BOTON_ARCHIVO2_X1, BOTON_ARCHIVO2_Y1, BOTON_ARCHIVO2_X2, BOTON_ARCHIVO2_Y2 = 3 * ANCHO_VENTANA // 4 - BOTON_X, BOTON_ARCHIVOS_Y - BOTON_Y, 3 * ANCHO_VENTANA // 4 + BOTON_X, BOTON_ARCHIVOS_Y + BOTON_Y #BOTON SELECCION ARCHIVO JUGADOR 2
BOTON_EQUIPO1_X1, BOTON_EQUIPO1_Y1, BOTON_EQUIPO1_X2, BOTON_EQUIPO1_Y2 = ANCHO_VENTANA // 4 - BOTON_X, BOTON_EQUIPOS_Y - BOTON_Y, ANCHO_VENTANA // 4 + BOTON_X, BOTON_EQUIPOS_Y + BOTON_Y #BOTON SELECCION EQUIPO JUGADOR 1
BOTON_EQUIPO2_X1, BOTON_EQUIPO2_Y1, BOTON_EQUIPO2_X2, BOTON_EQUIPO2_Y2 = 3 * ANCHO_VENTANA // 4 - BOTON_X, BOTON_EQUIPOS_Y - BOTON_Y, 3 * ANCHO_VENTANA // 4 + BOTON_X, BOTON_EQUIPOS_Y + BOTON_Y #BOTON SELECCION EQUIPO JUGADOR 2
SHOW_X1, SHOW_Y1, SHOW_X2, SHOW_Y2 = MITAD_X - BOTON_X, BOTON_FIN_ARCHIVOS_Y - BOTON_Y, MITAD_X + BOTON_X, BOTON_FIN_ARCHIVOS_Y + BOTON_Y


class ClaseEquipo():
    def __init__(self, diccionario):
        self.numero = diccionario['numero']
        self.nombre = diccionario['equipo_nombre']
        self.pokmov = lectores.pokemon_y_movimiento_a_tuplas(diccionario)

    def __str__(self):
        return 'Equipo número {}. Nombre {}. Pares de pokemones con sus movimientos {}'.format(self.numero, self.nombre, self.pokmov)

    def eliminar_pokemon_derrotado(self, derrotado):
        for par in self.pokmov:
            print (self.pokmov, par)
            if par[0] == derrotado.numero:
                self.pokmov.remove(par)


def menu_principio():
    """
    Dibuja el menú principal.
    """
    CREDITOS_X, CREDITOS_Y = ANCHO_VENTANA // 2, ALTO_VENTANA - 2 * TITULO_Y // 3  # POSICIÓN CREDITOS
    TEXTO_CENTRO_X, TEXTO_CENTRO_Y = MITAD_X, MITAD_Y

    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)  # FONDO BLANCO
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, FRANJA_AZUL_Y, fill=COLOR_AZUL)  # FRANJA SUPERIOR AZUL
    gamelib.draw_rectangle(VACIO, ALTO_VENTANA - FRANJA_AZUL_Y, ANCHO_VENTANA, ALTO_VENTANA, fill=COLOR_AZUL)  # FRANJA INFERIOR AZUL
    gamelib.draw_rectangle(BOTON_PRIMERMENU_X1, BOTON_PRIMERMENU_Y1, BOTON_PRIMERMENU_X2, BOTON_PRIMERMENU_Y2)  # BOTÓN TITULO "POKEMONES"
    gamelib.draw_text('POKEMON SHOWDOWN', MITAD_X, TITULO_Y, fill='white', size=30, anchor='s')  # TITULO
    gamelib.draw_text('De Ditto, Arean y Langer', CREDITOS_X, CREDITOS_Y, fill='white', size=10, anchor='n')  # CREDITOS
    gamelib.draw_text('COMENZAR', TEXTO_CENTRO_X, TEXTO_CENTRO_Y, fill='black', size=25, anchor='c')  # TEXTO "POKEMONES"
    gamelib.draw_end()

    return 'menu_principio', '', '', '', ''


def menu_archivos(ARCHIVO1, ARCHIVO2, EQUIPO1, EQUIPO2):
    """
    Dibuja el menú de selección de archivos y equipos.
    """
    BA1X1, BA1Y1, BA1X2, BA1Y2 = BOTON_ARCHIVO1_X1, BOTON_ARCHIVO1_Y1, BOTON_ARCHIVO1_X2, BOTON_ARCHIVO1_Y2
    BA2X1, BA2Y1, BA2X2, BA2Y2 = BOTON_ARCHIVO2_X1, BOTON_ARCHIVO2_Y1, BOTON_ARCHIVO2_X2, BOTON_ARCHIVO2_Y2
    BE1X1, BE1Y1, BE1X2, BE1Y2 = BOTON_EQUIPO1_X1, BOTON_EQUIPO1_Y1, BOTON_EQUIPO1_X2, BOTON_EQUIPO1_Y2
    BE2X1, BE2Y1, BE2X2, BE2Y2 = BOTON_EQUIPO2_X1, BOTON_EQUIPO2_Y1, BOTON_EQUIPO2_X2, BOTON_EQUIPO2_Y2
    TEXTO_NOMBRE_1 = ''
    TEXTO_NOMBRE_2 = ''
    if not EQUIPO1 == '': TEXTO_NOMBRE_1 = EQUIPO1['equipo_nombre']
    if not EQUIPO2 == '': TEXTO_NOMBRE_2 = EQUIPO2['equipo_nombre']

    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)  # FONDO BLANCO
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, FRANJA_AZUL_Y, fill=COLOR_AZUL)  # FRANJA SUPERIOR AZUL
    gamelib.draw_rectangle(VACIO, ALTO_VENTANA - FRANJA_AZUL_Y, ANCHO_VENTANA, ALTO_VENTANA, fill=COLOR_AZUL)  # FRANJA INFERIOR AZUL
    gamelib.draw_rectangle(BA1X1, BA1Y1, BA1X2, BA1Y2)  # BOTON SELECCION ARCHIVOS JUGADOR 1
    gamelib.draw_rectangle(BA2X1, BA2Y1, BA2X2, BA2Y2)  # BOTON SELECCION ARCHIVOS JUGADOR 2
    gamelib.draw_rectangle(BE1X1, BE1Y1, BE1X2, BE1Y2)  # BOTON SELECCION EQUIPOS JUGADOR 1
    gamelib.draw_rectangle(BE2X1, BE2Y1, BE2X2, BE2Y2)  # BOTON SELECCION EQUIPOS JUGADOR 2
    gamelib.draw_rectangle(SHOW_X1, SHOW_Y1, SHOW_X2, SHOW_Y2)  # BOTON ¡SHOWDOWN!
    gamelib.draw_text('SELECCIÓN DE EQUIPOS PARA JUGADOR 1 Y 2', MITAD_X, TITULO_Y, fill='white', size=28, anchor='s')  # TITULO
    gamelib.draw_text('ARCHIVO 1', BA1X1, BA1Y1, fill='black', size=25, anchor='nw')  # TEXTO "ARCHIVO 1"
    gamelib.draw_text('ARCHIVO 2', BA2X1, BA2Y1, fill='black', size=25, anchor='nw')  # TEXTO "ARCHIVO 2
    gamelib.draw_text('EQUIPO 1', BE1X1, BE1Y1, fill='black', size=25, anchor='nw')  # TEXTO "EQUIPO 1"
    gamelib.draw_text('EQUIPO 2', BE2X1, BE2Y1, fill='black', size=25, anchor='nw')  # TEXTO "EQUIPO 2"
    gamelib.draw_text('¡SHOWDOWN!', MITAD_X - BOTON_X, BOTON_FIN_ARCHIVOS_Y - BOTON_Y, fill='black', size=25, anchor='nw')  # TEXTO "¡SHOWDOWN!"
    gamelib.draw_text((ARCHIVO1), BA1X1, TEXTO_ARCHIVOS_Y - BOTON_Y, fill='black', size=25, anchor='nw') 
    gamelib.draw_text((ARCHIVO2), BA2X1, TEXTO_ARCHIVOS_Y - BOTON_Y, fill='black', size=25, anchor='nw')  
    gamelib.draw_text((TEXTO_NOMBRE_1), BE1X1, TEXTO_EQUIPOS_Y - BOTON_Y, fill='black', size=25, anchor='nw') 
    gamelib.draw_text((TEXTO_NOMBRE_2), BE2X1, TEXTO_EQUIPOS_Y - BOTON_Y, fill='black', size=25, anchor='nw')  
    gamelib.draw_end()

    return 'menu_archivos', ARCHIVO1, ARCHIVO2, EQUIPO1, EQUIPO2


def error():
    """Función para detectar errores en la navegacion"""
    gamelib.draw_begin()
    gamelib.draw_text('lol no', MITAD_X, MITAD_Y, fill='red', size=30, anchor='s')  # TITULO
    gamelib.draw_end()


def recibir_archivo_jugador():
    """
    Recibe qué archivo de equipos quiere usar un jugador.
    Se ingresa por parametro qué numero de jugador está eligiendo archivo.
    """
    ingreso = ''

    while not os.path.exists(ingreso):
        ingreso = gamelib.input(MENSAJE_INGRESE_RUTA)
        if ingreso == None:
            return ''
        if os.path.exists(ingreso):
            return ingreso
        gamelib.say(MENSAJE_ERROR_RUTA)


def recibir_equipo_jugador(ARCHIVO):
    """
    Recibe qué equipo quiere usar un jugador de todos los disponibles en el archivo eligido. 
    Se ingresa por parametro qué numero de jugador está eligiendo archivo.
    """
    while True:
        intento = gamelib.input(MENSAJE_INGRESE_NRO_EQUIPO)
        if intento == None:
            return ''
        if not intento.isdigit():
            continue

        busqueda = lectores.lector_por_numero(int(intento), ARCHIVO)
        if busqueda == None:
            gamelib.say(MENSAJE_ERROR_EQUIPO_INVALIDO)
            continue
        else: return busqueda


def botones_seleccion_archivos(x, y, ARCHIVO1, ARCHIVO2, EQUIPO1, EQUIPO2):
    """
    Según la posición del click recibido, elige el botón correcto y llama a la función.
    """
    BA1X1, BA1Y1, BA1X2, BA1Y2 = BOTON_ARCHIVO1_X1, BOTON_ARCHIVO1_Y1, BOTON_ARCHIVO1_X2, BOTON_ARCHIVO1_Y2  # ARCHIVO 1
    BA2X1, BA2Y1, BA2X2, BA2Y2 = BOTON_ARCHIVO2_X1, BOTON_ARCHIVO2_Y1, BOTON_ARCHIVO2_X2, BOTON_ARCHIVO2_Y2  # ARCHIVO 2
    BE1X1, BE1Y1, BE1X2, BE1Y2 = BOTON_EQUIPO1_X1, BOTON_EQUIPO1_Y1, BOTON_EQUIPO1_X2, BOTON_EQUIPO1_Y2  # EQUIPO 1
    BE2X1, BE2Y1, BE2X2, BE2Y2 = BOTON_EQUIPO2_X1, BOTON_EQUIPO2_Y1, BOTON_EQUIPO2_X2, BOTON_EQUIPO2_Y2  # EQUIPO 2
    if   BA1X1 < x < BA1X2 and BA1Y1 < y < BA1Y2:
        ARCHIVO1 = recibir_archivo_jugador()

    elif BA2X1 < x < BA2X2 and BA2Y1 < y < BA2Y2:
        ARCHIVO2 = recibir_archivo_jugador()

    elif BE1X1 < x < BE1X2 and BE1Y1 < y < BE1Y2:
        if ARCHIVO1 == '':
            gamelib.say(MENSAJE_ERROR_NECESITO_ARCHIVO) 
        else: EQUIPO1 = recibir_equipo_jugador(ARCHIVO1)

    elif BE2X1 < x < BE2X2 and BE2Y1 < y < BE2Y2:
        if ARCHIVO2 == '':
            gamelib.say(MENSAJE_ERROR_NECESITO_ARCHIVO) 
        else: EQUIPO2 = recibir_equipo_jugador(ARCHIVO2)

    elif SHOW_X1 < x < SHOW_X2 and SHOW_Y1 < y < SHOW_Y2:
        if not EQUIPO1 == '' and not EQUIPO2 == '':
            OBJ_EQUIPO1 = ClaseEquipo(EQUIPO1)
            OBJ_EQUIPO2 = ClaseEquipo(EQUIPO2)
            return "batalla", OBJ_EQUIPO1, OBJ_EQUIPO2 
        gamelib.say(MENSAJE_FALTA_EQUIPO) 

    return menu_archivos(ARCHIVO1, ARCHIVO2, EQUIPO1, EQUIPO2)


def navegacion(x, y, juego):
    """
    Navega en el programa según el click del usuario.
    """
    if juego[0] == 'menu_principio':
        if BOTON_PRIMERMENU_X1 < x <  BOTON_PRIMERMENU_X2  and BOTON_PRIMERMENU_Y1 < y < BOTON_PRIMERMENU_Y2:
            return menu_archivos(juego[1], juego[2], juego[3], juego[4])
        return menu_principio()

    if juego[0] == 'menu_archivos':
        return botones_seleccion_archivos(x, y, juego[1], juego[2], juego[3], juego[4])

    return error()
