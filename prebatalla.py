import gamelib
import batalla

ANCHO_VENTANA = batalla.ANCHO_VENTANA
ALTO_VENTANA = batalla.ALTO_VENTANA
MENU_MEMORIZADO = 'primer menu'
ARCHIVO1 = ''
ARCHIVO2 = ''
EQUIPO1 = ''
EQUIPO2 = ''

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

    global MENU_MEMORIZADO
    MENU_MEMORIZADO = 'menu_principio'
    return MENU_MEMORIZADO


def menu_archivos():
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
    gamelib.draw_text(('Archivo de J1: ' + ARCHIVO1), BA1X1, TEXTO_ARCHIVOS_Y - BOTON_Y, fill='black', size=25, anchor='nw') 
    gamelib.draw_text(('Archivo de J2: ' + ARCHIVO2), BA2X1, TEXTO_ARCHIVOS_Y - BOTON_Y, fill='black', size=25, anchor='nw')  
    gamelib.draw_text(('Equipo de J1: ' + EQUIPO1), BE1X1, TEXTO_EQUIPOS_Y - BOTON_Y, fill='black', size=25, anchor='nw') 
    gamelib.draw_text(('Equipo de J2: ' + EQUIPO2), BE2X1, TEXTO_EQUIPOS_Y - BOTON_Y, fill='black', size=25, anchor='nw')  
    gamelib.draw_end()

    global MENU_MEMORIZADO
    MENU_MEMORIZADO = 'menu_archivos'
    return MENU_MEMORIZADO


def error():
    gamelib.draw_begin()
    gamelib.draw_text('lol no', MITAD_X, MITAD_Y, fill='red', size=30, anchor='s')  # TITULO
    gamelib.draw_end()

    global MENU_MEMORIZADO
    MENU_MEMORIZADO = 'error'
    return MENU_MEMORIZADO


def recibir_archivo_jugador_1():
    print('96')
    # global ARCHIVO1
    # ARCHIVO1 = 


def recibir_archivo_jugador_2():
    print('101')


def recibir_equipo_jugador_1():
    print('104')


def recibir_equipo_jugador_2():
    print('108')


def botones_seleccion_archivos(x, y):
    BA1X1, BA1Y1, BA1X2, BA1Y2 = BOTON_ARCHIVO1_X1, BOTON_ARCHIVO1_Y1, BOTON_ARCHIVO1_X2, BOTON_ARCHIVO1_Y2  # ARCHIVO 1
    BA2X1, BA2Y1, BA2X2, BA2Y2 = BOTON_ARCHIVO2_X1, BOTON_ARCHIVO2_Y1, BOTON_ARCHIVO2_X2, BOTON_ARCHIVO2_Y2  # ARCHIVO 2
    BE1X1, BE1Y1, BE1X2, BE1Y2 = BOTON_EQUIPO1_X1, BOTON_EQUIPO1_Y1, BOTON_EQUIPO1_X2, BOTON_EQUIPO1_Y2  # EQUIPO 1
    BE2X1, BE2Y1, BE2X2, BE2Y2 = BOTON_EQUIPO2_X1, BOTON_EQUIPO2_Y1, BOTON_EQUIPO2_X2, BOTON_EQUIPO2_Y2  # EQUIPO 2
    if   BA1X1 < x < BA1X2 and BA1Y1 < y < BA1Y2:
        recibir_archivo_jugador_1()
    elif BA2X1 < x < BA2X2 and BA2Y1 < y < BA2Y2:
        recibir_archivo_jugador_2()
    elif BE1X1 < x < BE1X2 and BE1Y1 < y < BE1Y2:
        recibir_equipo_jugador_1()
    elif BE2X1 < x < BE2X2 and BE2Y1 < y < BE2Y2:
        recibir_equipo_jugador_2()
    elif SHOW_X1 < x < SHOW_X2 and SHOW_Y1 < y < SHOW_Y2:
        if not EQUIPO1 == '' and not EQUIPO2 == '':
            batalla.desarrollo_combate(EQUIPO1, EQUIPO2)  # AQUI LLAMA AL PROXIMO ARCHIVO UNA VEZ TIENE DOS EQUIPOS
        else:
            gamelib.say('No se eligieron dos equipos aún.') 


def navegacion(x, y, juego):
    
    if juego == 'menu_principio':
        if BOTON_PRIMERMENU_X1 < x <  BOTON_PRIMERMENU_X2  and BOTON_PRIMERMENU_Y1 < y < BOTON_PRIMERMENU_Y2:
            return menu_archivos()
        return menu_principio()

    if juego == 'menu_archivos':
        botones_seleccion_archivos(x, y)
        return menu_archivos()

    if juego == 'error':
        return error()

    return error()
