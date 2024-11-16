import random

import utils

TIPOS_DE_EVENTOS = ["CASAMIENTO", "QUINCE", "CUMPLE", "BAUTISMO", "OTRO"]
MAXIMO_EVENTOS_POR_FECHA = 10
id_utilizadas = []
fechasUtilizadas = []


def idRandom():
    id = random.randint(1000, 9999)
    while utils.elementoEnLista(id, id_utilizadas):
        id = random.randint(1000, 9999)
    return id


def generarDiaValido(mes, anio):
    bis = utils.anioBisiesto(anio)
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
        identificador = idRandom()

        evento = [identificador, dia, mes, anio, tipoDeEvento, cantidadDeFotos]
        eventos.append(evento)

    return eventos


def costo(evento):
    costo_fotos = evento[5] * 50  # cantidad de fotos * $50
    match evento[4]:
        case "CASAMIENTO":
            return costo_fotos + 50000
        case "QUINCE":
            return costo_fotos + 60000
        case "CUMPLE":
            return costo_fotos + 35000
        case "BAUTISMO":
            return costo_fotos + 38000
        case _:
            return costo_fotos + 25000


def facturar(evento):
    """
    Esta funcion devuelve cuanto debe facturarse el evento
    """
    cantidad_fotos = evento[5]
    match evento[4]:
        case "CASAMIENTO":
            costo_base = 50000
            if cantidad_fotos <= 500:
                return costo_base + (750 * cantidad_fotos)
            elif 500 < cantidad_fotos < 1000:
                return costo_base + (650 * cantidad_fotos)
            elif cantidad_fotos > 1000:
                return costo_base + (600 * cantidad_fotos)
        case "QUINCE":
            costo_base = 60000
            if cantidad_fotos <= 500:
                return costo_base + (850 * cantidad_fotos)
            elif 500 < cantidad_fotos < 1000:
                return costo_base + (750 * cantidad_fotos)
            elif cantidad_fotos > 1000:
                return costo_base + (700 * cantidad_fotos)
        case "CUMPLE":
            costo_base = 35000
            if cantidad_fotos <= 500:
                return costo_base + (650 * cantidad_fotos)
            elif 500 < cantidad_fotos:
                return costo_base + (550 * cantidad_fotos)
        case "BAUTISMO":
            costo_base = 38000
            if cantidad_fotos <= 500:
                return costo_base + (750 * cantidad_fotos)
            elif 500 < cantidad_fotos:
                return costo_base + (650 * cantidad_fotos)
        case _:
            costo_base = 25000
            if cantidad_fotos <= 500:
                return costo_base + (1000 * cantidad_fotos)
            elif 500 < cantidad_fotos < 1000:
                return costo_base + (900 * cantidad_fotos)
            elif cantidad_fotos > 1000:
                return costo_base + (800 * cantidad_fotos)


def promedioDeFotos(eventos):
    totalFotos = 0
    for evento in eventos:
        totalFotos += evento[5]
    return totalFotos // len(eventos)

