import csv
from tkinter.constants import E


def lector_por_numero(nro, nombre_archivo, delimitador=';'):
    """
    Lee el archivo ingresado por parámetro y retorna la linea que tiene el número buscado en su columna 'numero'.
    La linea es retornada en forma de diccionario con los encabezados como llaves.
    """
    if type(nro) is int:
        nro = str(nro)

    with open(nombre_archivo) as archivo:
        reader = csv.DictReader(archivo, delimiter=delimitador)

        for linea in reader:
            if linea['numero'] == nro:
                return linea


def lector_por_nombre(movimiento, archivo, delimitador=','):
    """
    Lee el archivo ingresado por parámetro y retorna la linea que tiene el nombre buscado en su columna 'nombre'.
    La linea es retornada en forma de diccionario con los encabezados como llaves.
    """
    with open(archivo) as archivo:
        reader = csv.DictReader(archivo, delimiter=delimitador)

        for linea in reader:
            if linea['nombre'] == movimiento:
                return linea


def pokemon_y_movimiento_a_tuplas(equipo):
    """
    Recibe un equipo en forma de diccionario y retorna una lista con tuplas. 
    Cada tupla tiene un par de elementos, un pokemon y sus movimientos.
    """
    resultado = []
    encabezados = ('integrante1', 'movimientos1'), ('integrante2', 'movimientos2'), ('integrante3', 'movimientos3'), ('integrante4', 'movimientos4'), ('integrante5', 'movimientos5'), ('integrante6', 'movimientos6')
    for elemento in encabezados:
        if elemento[0] in equipo:
            resultado.append((equipo[elemento[0]], equipo[elemento[1]]))

    return resultado


def detalles_tipos(tipo, archivo, delimitador=';'):
    """
    Lee el archivo ingresado por parámetro y retorna la linea que tiene el nombre buscado en su columna 'Types'.
    La linea es retornada en forma de diccionario con los encabezados como llaves.
    """
    with open(archivo) as archivo:
        reader = csv.DictReader(archivo, delimiter=delimitador)

        for linea in reader:
            if linea['Types'] == tipo:
                return linea
