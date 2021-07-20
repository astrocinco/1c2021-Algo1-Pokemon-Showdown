import gamelib

ANCHO_VENTANA = 900
ALTO_VENTANA = 600
menu_memorizado = 'primer menu'

MITAD_X = ANCHO_VENTANA // 2
MITAD_Y = ALTO_VENTANA // 2
VACIO = 0
FRANJA_AZUL_Y = 88
COLOR_AZUL = '#0d1364'
TITULO_Y = 70
BOTON_X = 120
BOTON_Y = 25
BOTON_PRIMERMENU_X1, BOTON_PRIMERMENU_Y1, BOTON_PRIMERMENU_X2, BOTON_PRIMERMENU_Y2 = MITAD_X - BOTON_X, MITAD_Y - BOTON_Y, MITAD_X + BOTON_X, MITAD_Y + BOTON_Y #POSICION BOTON CENTRAL PRIMER MENU


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

    global menu_memorizado
    menu_memorizado = 'menu_principio'
    return menu_memorizado


def error():
    gamelib.draw_begin()
    gamelib.draw_text('lol no', MITAD_X, MITAD_Y, fill='red', size=30, anchor='s')  # TITULO
    gamelib.draw_end()

    global menu_memorizado
    menu_memorizado = 'error'
    return menu_memorizado


def navegacion(x, y, juego):
    if juego == 'menu_principio':
        if BOTON_PRIMERMENU_X1 < x <  BOTON_PRIMERMENU_X2  and BOTON_PRIMERMENU_Y1 < y < BOTON_PRIMERMENU_Y2:
            return menu_principio()

    if juego == 'error':
        return error()

    return error()
