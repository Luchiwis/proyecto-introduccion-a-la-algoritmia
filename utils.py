import random


def elementoEnLista(x, lista):  # Complejidad Omega(n)   Siendo n = longitud de lista
    esta = False
    iter = 0
    while iter < len(lista):
        if lista[iter] == x:
            esta = True
        iter += 1
    return esta


def contarRepeticiones(elemento, lista):
    repes = 0
    iter = 0
    while iter < len(lista):
        if lista[iter] == elemento:
            repes += 1
        iter += 1
    return repes


def choice(lista):
    if lista:
        return lista[random.randint(0, len(lista) - 1)]


def imprimirMenu():
    print()
    print("********************************************")
    print("Debe elegir una opcion, solo numeros enteros")
    print("1 - Totales mes")
    print("2 - Total por tipo de evento")
    print("3 - Detalle por evento")
    print("4 - Detalle por mes")
    print("5 - Detalle del día")
    print("6 - SALIR")
    print("********************************************")
    print()


def queMes(mes):
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
        "Diciembre"
    ]
    cual = meses[mes]
    return cual
