import csv


def lector_por_numero(nro, nombre_archivo):
    """
    Lee el archivo ingresado por parametro, ignora la primera linea y retorna un diccionario con el numero de linea como llave.
    El diccionario contiene toda la información de la linea solicitada como lista.
    Retorna la información de solo un pokemon.
    """
    contador = -1
    with open(nombre_archivo) as archivo:
        for linea in archivo:
            leido = linea#.readline()
            contador += 1
            if contador == nro:
                print (nro, nombre_archivo, leido)
                return leido[:-1].split(';')


def extraer_integrantes_equipo(equipo):
    resultado = []

    resultado.append(equipo[2])
    resultado.append(equipo[4])
    resultado.append(equipo[6])
    #resultado.append(equipo[8])
    #resultado.append(equipo[10])
    #resultado.append(equipo[12]) # REHACER PARA CUALQUIER TAMAÑO DE EQUIPO
    return resultado


def movimiento_en_pokemon(numero, archivo):
    return 1 # HACER
