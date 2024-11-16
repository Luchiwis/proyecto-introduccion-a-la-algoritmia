"""
Archivo con funcionalidades miscelaneas. Mayormente funciones que no podemos usar y tenemos que resolver manualmente
"""

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


def multiplicarString(string, n):
    """
    esta funcion sirve para hacer string*n pero manualmente, ya que no sabemos si está permitido utilizar la primera tecnica
    """

    msg = ""
    for _ in range(n):
        msg += string
    return msg