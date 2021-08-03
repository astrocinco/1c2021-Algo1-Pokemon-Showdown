import prebatalla
import batalla

def main():
    prebatalla.gamelib.resize(prebatalla.ANCHO_VENTANA, prebatalla.ALTO_VENTANA)
    prebatalla.gamelib.title('Pokemon Showdown! - Selección de equipos')
    juego = 'menu_principio', None, None, None, None
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

        if juego[0] == 'batalla':
                batalla.gamelib.title('Pokemon Showdown! - Combate')
                batalla.desarrollo_combate(juego[1], juego[2]) 

prebatalla.gamelib.init(main) 
