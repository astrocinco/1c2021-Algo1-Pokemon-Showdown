import showdown

def main():
    showdown.gamelib.resize(showdown.ANCHO_VENTANA, showdown.ALTO_VENTANA)
    juego = 'menu_principio'
    showdown.menu_principio()

    while showdown.gamelib.is_alive():
        ev = showdown.gamelib.wait()

        if not ev:
            break

        if ev.type == showdown.gamelib.EventType.KeyPress and ev.key == 'Escape':      
            break

        if ev.type == showdown.gamelib.EventType.ButtonPress:
            x, y = ev.x, ev.y
            juego = showdown.navegacion(x, y, juego)

showdown.gamelib.init(main) 
