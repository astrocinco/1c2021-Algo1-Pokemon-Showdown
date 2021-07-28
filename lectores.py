import csv


def lector_por_numero(nro, nombre_archivo):
    """
    Lee el archivo ingresado por parametro, ignora la primera linea y retorna un diccionario con el numero de linea como llave.
    El diccionario contiene toda la información de la linea solicitada como lista.
    Retorna la información de solo un pokemon.
    """
    if type(nro) is str:
        nro = int(nro)
    contador = -1
    
    with open(nombre_archivo) as archivo:
        for linea in archivo:
            leido = linea
            contador += 1

            if contador == nro:
                return leido[:-1].split(';')


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
<<<<<<< HEAD

def detalles_tipos(tipo, archivo):
    with open(archivo) as archivo:
        reader = csv.DictReader(archivo)

        for linea in reader:
            if linea['Types'] == tipo:
                return linea
=======
        raise Exception ('El movimiento no fue encontrado en el archivo.')
>>>>>>> 0825e0cbb2e4916310d52435475879412d410128
