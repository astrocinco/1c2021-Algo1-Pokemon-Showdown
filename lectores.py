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


def movimiento_en_pokemon(numero, archivo):
    return 1 # HACER

print (lector_por_numero(37, 'equipos.csv'))