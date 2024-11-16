"""
funciones relacionadas con fechas
"""

def queMes(mes):
    mes = int(mes)
    "convierte el mes de numero a palabra"
    meses = [
        None,
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre",
    ]
    cual = meses[mes]
    return cual


def anioBisiesto(anio):
    # determina si un año es bisiesto
    if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        return True
    else:
        return False


def validarFecha(dia, mes, anio):
    """
    devuelve True si el dia es valido
    """
    maxDias = 0
    if mes == 2 and anioBisiesto(anio):
        maxDias = 29
    else:
        dias = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        maxDias = dias[mes]

    if 0 < dia <= maxDias:
        return True
    else:
        return False
