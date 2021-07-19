import gamelib

ANCHO_VENTANA = 900
ALTO_VENTANA = 600

#BOTON_PRIMERO = 


def primer_menu():
    """
    Dibuja el menú principal.
    """
    CREDITOS_X, CREDITOS_Y = ANCHO_VENTANA // 2, ALTO_VENTANA - 2 * TITLE_Y // 3  # POSICIÓN CREDITOS
    BOTON_IZQ_X1, BOTON_IZQ_Y1, BOTON_IZQ_X2, BOTON_IZQ_Y2 = MARGEN_ENTRE_BOTONES, BOTON_Y1, ANCHO_VENTANA // 2 - ESPACIO_ENTRE_BOTONES, BOTON_Y2
    BOTON_DER_X1, BOTON_DER_Y1, BOTON_DER_X2, BOTON_DER_Y2 = ANCHO_VENTANA // 2 + ESPACIO_ENTRE_BOTONES, BOTON_Y1, ANCHO_VENTANA - MARGEN_ENTRE_BOTONES, BOTON_Y2
    TEXTO_IZQ_X, TEXTO_IZQ_Y = MARGEN_ENTRE_BOTONES * 2, ALTO_VENTANA // 2 - 5 * ALTO_BOTONES // 6
    TEXTO_DER_X, TEXTO_DER_Y = ANCHO_VENTANA // 2 + 2 * ESPACIO_ENTRE_BOTONES + MARGEN_ENTRE_BOTONES, ALTO_VENTANA // 2 - 5 * ALTO_BOTONES // 6

    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)  # FONDO BLANCO
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, FRANJA_AZUL_Y, fill='#0d1364')  # FRANJA SUPERIOR AZUL
    gamelib.draw_rectangle(VACIO, ALTO_VENTANA - FRANJA_AZUL_Y, ANCHO_VENTANA, ALTO_VENTANA, fill='#0d1364')  # FRANJA INFERIOR AZUL
    gamelib.draw_rectangle(BOTON_IZQ_X1, BOTON_IZQ_Y1, BOTON_IZQ_X2, BOTON_IZQ_Y2)  # BOTÓN TITULO "POKEMONES"
    gamelib.draw_rectangle(BOTON_DER_X1, BOTON_DER_Y1, BOTON_DER_X2, BOTON_DER_Y2)  # BOTÓN TITULO "EQUIPOS"
    gamelib.draw_text('POKEDEX', ANCHO_VENTANA // 2, TITLE_Y, fill='white', size=30, anchor='s')  # TITULO
    gamelib.draw_text('De Ditto, Arean y Langer', CREDITOS_X, CREDITOS_Y, fill='white', size=10, anchor='n')  # CREDITOS
    gamelib.draw_text('POKEMONES', TEXTO_IZQ_X, TEXTO_IZQ_Y, fill='black', size=25, anchor='nw')  # TEXTO "POKEMONES"
    gamelib.draw_text('EQUIPOS', TEXTO_DER_X, TEXTO_DER_Y, fill='black', size=25, anchor='nw')  # TEXTO "EQUIPOS"
    gamelib.draw_end()

    return 'primer menu'


def navegacion(x, y, juego):
    if juego == 'primer menu':
        primer_menu()