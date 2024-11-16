"""
funciones relativas a los eventos
"""

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