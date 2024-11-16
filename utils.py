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


def ordenarTabla(datos, indice):
    """
    devuelve una tabla ordenada en base al valor del índice dado utilizando Bubble Sort
    ignora la primera fila ya que esta es la de los titulos y contiene solo strings
    """
    n = len(datos)
    for i in range(n):
        for j in range(1, n - i - 1):
            if datos[j][indice] > datos[j + 1][indice]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
    return datos


def mostrarTabla(datos):
    """
    es una funcion para mostrar una lista de datos como una tabla de manera prolija
    """
    cantidad_columnas = len(datos[0])

    # inicializar la lista con 0 para poder comparar
    maximo_por_columna = []
    for i in range(cantidad_columnas):
        maximo_por_columna.append(0)

    # comparar y buscar el maximo de caracteres por cada columna
    for fila in datos:
        for i in range(len(fila)):
            dato = str(fila[i])
            if len(dato) > maximo_por_columna[i]:
                maximo_por_columna[i] = len(dato)

    # mostrar datos
    for fila in datos:
        mostrar_fila = ""
        for i in range(len(fila)):
            dato = str(fila[i])
            mostrar_celda = (
                "|"
                + " "
                + dato
                + multiplicarString(" ", maximo_por_columna[i] - len(dato))
                + " "
                + "|"
            )
            mostrar_fila += mostrar_celda
        print(mostrar_fila)

    # print(maximo_por_columna)
    # for dato in datos:
    #     print(dato)

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
