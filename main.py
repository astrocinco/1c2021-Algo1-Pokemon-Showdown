import prebatalla
import batalla

def main():
    prebatalla.gamelib.resize(prebatalla.ANCHO_VENTANA, prebatalla.ALTO_VENTANA)
    juego = 'menu_principio', '', ''
    prebatalla.menu_principio()

    while prebatalla.gamelib.is_alive():
        ev = prebatalla.gamelib.wait()

        if not ev:
            break

        if ev.type == prebatalla.gamelib.EventType.KeyPress and ev.key == 'Escape':      
            break

        if ev.type == prebatalla.gamelib.EventType.ButtonPress:
            x, y = ev.x, ev.y

            if juego[0] == 'batalla':
                batalla.desarrollo_combate(juego[1], juego[2]) 

            juego = prebatalla.navegacion(x, y, juego)

prebatalla.gamelib.init(main) 
