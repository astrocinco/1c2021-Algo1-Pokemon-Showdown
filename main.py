import prebatalla

def main():
    prebatalla.gamelib.resize(prebatalla.ANCHO_VENTANA, prebatalla.ALTO_VENTANA)
    juego = 'menu_principio'
    prebatalla.menu_principio()

    while prebatalla.gamelib.is_alive():
        ev = prebatalla.gamelib.wait()

        if not ev:
            break

        if ev.type == prebatalla.gamelib.EventType.KeyPress and ev.key == 'Escape':      
            break

        if ev.type == prebatalla.gamelib.EventType.ButtonPress:
            x, y = ev.x, ev.y
            juego = prebatalla.navegacion(x, y, juego)

prebatalla.gamelib.init(main) 
