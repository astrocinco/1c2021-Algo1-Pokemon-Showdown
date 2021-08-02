import csv
from tkinter.constants import E


def lector_por_numero(nro, nombre_archivo):
    """
    Lee el archivo ingresado por parametro, ignora la primera linea y retorna un diccionario con el numero de linea como llave.
    El diccionario contiene toda la información de la linea solicitada como lista.
    Retorna la información de solo un pokemon.
    """
    if type(nro) is int:
        nro = str(nro)

    with open(nombre_archivo) as archivo:
        reader = csv.DictReader(archivo, delimiter=';')

        for linea in reader:
            #print (linea['numero'], type(linea['numero']), nro, type(nro))
            if linea['numero'] == nro:
                return linea
        #raise Exception ('El movimiento no fue encontrado en el archivo.')

    """
    contador = -1

    if type(nro) is str:
        nro = int(nro)

    if nro < 1:
        return
    
    with open(nombre_archivo) as archivo:
        for linea in archivo:
            contador += 1

            if contador == nro:
                return linea[:-1].split(';')
    """

def pokemon_y_movimiento_a_tuplas(equipo):
    """
    Recibe una linea del csv en forma de lista y retorna una lista con tuplas. 
    Cada tupla tiene un par de elementos, un pokemon y sus movimientos.
    """
    resultado = []
    encabezados = ('integrante1', 'movimientos1'), ('integrante2', 'movimientos2'), ('integrante3', 'movimientos3'), ('integrante4', 'movimientos4'), ('integrante5', 'movimientos5'), ('integrante6', 'movimientos6')
    for elemento in encabezados:
        if elemento[0] in equipo:
            resultado.append((equipo[elemento[0]], equipo[elemento[1]]))
    #for i in range(2, len(equipo), 2):
     #   if equipo[i] == '': continue
      #  resultado.append((equipo[i], equipo[i+1]))

    return resultado


def extraer_integrantes_equipo(equipo):
    """
    Recibe una lista con toda la información de un equipo.
    Retorna una lista de números de pokemones. 
    """
    resultado = []

    for i in range (2, len(equipo), 2):
        if equipo[i] == '': continue
        resultado.append(equipo[i])

    return resultado


def movimiento_en_pokemon(lista, numero):
    indice_pokemon = lista[2:].index(str(numero))
    opciones = lista[indice_pokemon + 3]

    return opciones


def detalles_movimiento(movimiento, archivo):
    with open(archivo) as archivo:
        reader = csv.DictReader(archivo)

        for linea in reader:
            if linea['nombre'] == movimiento:
                return linea

def detalles_tipos(tipo, archivo):
    with open(archivo) as archivo:
        reader = csv.DictReader(archivo)

        for linea in reader:
            if linea['Types'] == tipo:
                return linea
        raise Exception ('El movimiento no fue encontrado en el archivo.')
