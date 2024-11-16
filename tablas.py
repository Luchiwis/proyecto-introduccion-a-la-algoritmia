"""
Funciones que utilizamos para mostrar, ordenar y modificar tablas.
"""

import utils

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
                + utils.multiplicarString(" ", maximo_por_columna[i] - len(dato))
                + " "
                + "|"
            )
            mostrar_fila += mostrar_celda
        print(mostrar_fila)


def aplicarSignoPesos(tabla, columna):
    for i in range(1,len(tabla)): #ignora la primera fila
        fila = tabla[i]
        fila[columna] = "$" + str(fila[columna])
    return tabla