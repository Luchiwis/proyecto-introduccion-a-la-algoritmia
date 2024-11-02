import random

import utils

TIPOS_DE_EVENTOS = ["CASAMIENTO", "15", "CUMPLE", "BAUTISMO", "OTRO"]
MAXIMO_EVENTOS_POR_FECHA = 10
id_utilizadas = []
fechasUtilizadas = []


def idRandom():
    id = random.randint(1000, 9999)
    while utils.elementoEnLista(id, id_utilizadas):
        id = random.randint(1000, 9999)
    return id


def anioBisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        return True
    else:
        return False


def diaValido(mes, anio):
    bis = anioBisiesto(anio)
    maxDias = 0
    if mes == 2 and bis:
        maxDias = 29
    else:
        dias = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        maxDias = dias[mes]
    devolver = random.randint(1, maxDias)
    return devolver


def diaRandom(mes, anio):
    # chequear si el dia no se repite 5 veces
    fecha = [diaValido(mes, anio), mes, anio]
    while utils.contarRepeticiones(fecha, fechasUtilizadas) >= MAXIMO_EVENTOS_POR_FECHA:
        fecha = [diaValido(mes, anio), mes, anio]
    fechasUtilizadas.append(fecha)

    return fecha[0]

def generarDatos(mes, anio):
    """
    esta funcion devuelve un dato con el siguiente formato:
    [
        [id, dia, mes, año, tipo_de_evento, cantidad_fotos],
        ...
    ]

    Datos:
    - id (random) -> identificador (id es el nombre de una funcion reservada)
    - dia(random choice validado)
    - mes (parametro)
    - año (parametro)
    - tipo_de_evento (random choice)
    - cantidad_fotos (randint)

    Requisitos:
    - Validar mes y año

    Restricciones para la salida:
    - Entre 40 y 250 eventos.
    - Maximo de 10 eventos por fecha
    - 300 <= cantidad de fotos <= 5000
    - Id no se pueden repetir
    - 1000 <= ID <= 9999
    - Fechas validas

    Pasos:
    1- Generar una matriz de n filas siendo n = numero random entre 40 y 250 y 4 columnas [id, fecha, tipo_de_evento, cantidad_fotos]
    a partir del mes y el año que toma la funcion
    2- Generar los datos a

    """

    cantidadEventos = random.randint(40, 250)

    eventos = []

    for i in range(cantidadEventos):
        cantidadDeFotos = random.randint(300, 5000)
        tipoDeEvento = utils.choice(TIPOS_DE_EVENTOS)
        dia = diaValido()
        identificador = idRandom()
        
        evento = [identificador, dia, mes, anio, tipo_de_evento, cantidad_fotos]
        eventos.append(evento)
        

    return eventos


