import gamelib
import batalla
import lectores

ANCHO_VENTANA = batalla.ANCHO_VENTANA
ALTO_VENTANA = batalla.ALTO_VENTANA

MENSAJE_INGRESE_RUTA = "Ingrese el nombre o la ruta en la que tiene sus equipos"
MENSAJE_ERROR_RUTA = "No se encontró un archivo con ese nombre o ruta"
MENSAJE_INGRESE_NRO_EQUIPO = "Ingrese el numero de equipo con el que va a jugar"
MENSAJE_ERROR_NRO = "No ingreso un numero. Ingrese el numero de equipo con el que va a jugar"
MENSAJE_ERROR_EQUIPO_INVALIDO = "No ingreso un equipo valido"

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

    return 'menu_principio', '', '', ['', ''], ['', '']


def menu_archivos(ARCHIVO1, ARCHIVO2, EQUIPO1, EQUIPO2):
    """
    Dibuja el menú de selección de archivos y equipos.
    """
    BA1X1, BA1Y1, BA1X2, BA1Y2 = BOTON_ARCHIVO1_X1, BOTON_ARCHIVO1_Y1, BOTON_ARCHIVO1_X2, BOTON_ARCHIVO1_Y2
    BA2X1, BA2Y1, BA2X2, BA2Y2 = BOTON_ARCHIVO2_X1, BOTON_ARCHIVO2_Y1, BOTON_ARCHIVO2_X2, BOTON_ARCHIVO2_Y2
    BE1X1, BE1Y1, BE1X2, BE1Y2 = BOTON_EQUIPO1_X1, BOTON_EQUIPO1_Y1, BOTON_EQUIPO1_X2, BOTON_EQUIPO1_Y2
    BE2X1, BE2Y1, BE2X2, BE2Y2 = BOTON_EQUIPO2_X1, BOTON_EQUIPO2_Y1, BOTON_EQUIPO2_X2, BOTON_EQUIPO2_Y2

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
    gamelib.draw_text((EQUIPO1[1]), BE1X1, TEXTO_EQUIPOS_Y - BOTON_Y, fill='black', size=25, anchor='nw') 
    gamelib.draw_text((EQUIPO2[1]), BE2X1, TEXTO_EQUIPOS_Y - BOTON_Y, fill='black', size=25, anchor='nw')  
    gamelib.draw_end()

    return 'menu_archivos', ARCHIVO1, ARCHIVO2, EQUIPO1, EQUIPO2


def error():
    """Función para detectar errores en la navegacion"""
    gamelib.draw_begin()
    gamelib.draw_text('lol no', MITAD_X, MITAD_Y, fill='red', size=30, anchor='s')  # TITULO
    gamelib.draw_end()


def recibir_archivo_jugador(nro_jugador):
    """
    Recibe qué archivo de equipos quiere usar un jugador.
    Se ingresa por parametro qué numero de jugador está eligiendo archivo.
    """
    ingreso = gamelib.input(MENSAJE_INGRESE_RUTA)

    try:
        with open(ingreso, "r") as equipo:
            lector_equipo = lectores.csv.reader(equipo)
            if nro_jugador == 1:
                return ingreso
            if nro_jugador == 2:
                return ingreso
    except:
        gamelib.say(MENSAJE_ERROR_RUTA)


def recibir_equipo_jugador(nro_jugador, ARCHIVO1, ARCHIVO2):
    """
    Recibe qué equipo quiere usar un jugador de todos los disponibles en el archivo eligido. 
    Se ingresa por parametro qué numero de jugador está eligiendo archivo.
    """
    try:
        equipo_elegido = gamelib.input(MENSAJE_INGRESE_NRO_EQUIPO)
        while not equipo_elegido.isdigit():
            equipo_elegido = gamelib.input(MENSAJE_ERROR_NRO)
    except:
        gamelib.say(MENSAJE_ERROR_EQUIPO_INVALIDO)

    if nro_jugador == 1:
        return lectores.lector_por_numero(int(equipo_elegido), ARCHIVO1)

    if nro_jugador == 2:
        return lectores.lector_por_numero(int(equipo_elegido), ARCHIVO2)


def botones_seleccion_archivos(x, y, ARCHIVO1, ARCHIVO2, EQUIPO1, EQUIPO2):
    """
    Según la posición del click recibido, elige el botón correcto y llama a la función.
    """
    BA1X1, BA1Y1, BA1X2, BA1Y2 = BOTON_ARCHIVO1_X1, BOTON_ARCHIVO1_Y1, BOTON_ARCHIVO1_X2, BOTON_ARCHIVO1_Y2  # ARCHIVO 1
    BA2X1, BA2Y1, BA2X2, BA2Y2 = BOTON_ARCHIVO2_X1, BOTON_ARCHIVO2_Y1, BOTON_ARCHIVO2_X2, BOTON_ARCHIVO2_Y2  # ARCHIVO 2
    BE1X1, BE1Y1, BE1X2, BE1Y2 = BOTON_EQUIPO1_X1, BOTON_EQUIPO1_Y1, BOTON_EQUIPO1_X2, BOTON_EQUIPO1_Y2  # EQUIPO 1
    BE2X1, BE2Y1, BE2X2, BE2Y2 = BOTON_EQUIPO2_X1, BOTON_EQUIPO2_Y1, BOTON_EQUIPO2_X2, BOTON_EQUIPO2_Y2  # EQUIPO 2
    if   BA1X1 < x < BA1X2 and BA1Y1 < y < BA1Y2:
        ARCHIVO1 = recibir_archivo_jugador(1)
    elif BA2X1 < x < BA2X2 and BA2Y1 < y < BA2Y2:
        ARCHIVO2 = recibir_archivo_jugador(2)
    elif BE1X1 < x < BE1X2 and BE1Y1 < y < BE1Y2:
        EQUIPO1 = recibir_equipo_jugador(1, ARCHIVO1, ARCHIVO2)
    elif BE2X1 < x < BE2X2 and BE2Y1 < y < BE2Y2:
        EQUIPO2 = recibir_equipo_jugador(2, ARCHIVO1, ARCHIVO2)
    elif SHOW_X1 < x < SHOW_X2 and SHOW_Y1 < y < SHOW_Y2:
        if not EQUIPO1 == ['', ''] and not EQUIPO2 == ['', '']:
            return "batalla", EQUIPO1, EQUIPO2 # AQUI LLAMA AL PROGRAMA DE COMBATE EN MAIN UNA VEZ SE TIENE DOS EQUIPOS 
        gamelib.say('No se eligieron dos equipos aún.') 
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
