def color_barra(porcentaje):
    """Cambia el color de la barra de salud"""
    if porcentaje >= 0.8:
        color = 'green'

    if 0.3 < porcentaje < 0.8:
        color = 'orange'
        
    if porcentaje <= 0.3:
        color = 'red'
    
    return color
