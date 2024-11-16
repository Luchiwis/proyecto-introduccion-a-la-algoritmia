"""
Funciones relacionadas con la generacion de datos aleatorios
"""

import random
import utils
import fechas

TIPOS_DE_EVENTOS = ["CASAMIENTO", "QUINCE", "CUMPLE", "BAUTISMO", "OTRO"]
MAXIMO_EVENTOS_POR_FECHA = 10
id_utilizadas = []
fechasUtilizadas = []


def generarIDRandom():
    id = random.randint(1000, 9999)
    while utils.elementoEnLista(id, id_utilizadas):
        id = random.randint(1000, 9999)
    return id


def generarDiaValido(mes, anio):
    maxDias = 0
    if mes == 2 and fechas.anioBisiesto(anio):
        maxDias = 29
    else:
        dias = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        maxDias = dias[mes]
    devolver = random.randint(1, maxDias)
    return devolver
    

def diaRandom(mes, anio):
    # chequear si el dia no se repite 10 veces
    fecha = [generarDiaValido(mes, anio), mes, anio]
    while utils.contarRepeticiones(fecha, fechasUtilizadas) >= MAXIMO_EVENTOS_POR_FECHA:
        fecha = [generarDiaValido(mes, anio), mes, anio]
    fechasUtilizadas.append(fecha)

    return fecha[0]


def generarEventos(mes, anio):
    """esta funcion devuelve un dato con el siguiente formato:
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

    """

    cantidadEventos = random.randint(40, 250)

    eventos = []

    for _ in range(cantidadEventos):
        cantidadDeFotos = random.randint(300, 5000)
        tipoDeEvento = utils.choice(TIPOS_DE_EVENTOS)
        dia = generarDiaValido(mes, anio)
        identificador = generarIDRandom()

        evento = [identificador, dia, mes, anio, tipoDeEvento, cantidadDeFotos]
        eventos.append(evento)

    return eventos

