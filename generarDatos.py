import random


def generarDatos(mes, ano):
    """
    esta funcion devuelve un dato con el siguiente formato:
    [
        [id, dia, mes, año, tipo_de_evento, cantidad_fotos],
        ...
    ]
    
    Datos:
    - id (random)
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
    - 300 < cantidad de fotos < 5000  
    - Id no se pueden repetir
    - 1000 <= ID <= 9999
    - Fechas validas

    Pasos:
    1- Generar una matriz de n filas siendo n = numero random entre 40 y 250 y 4 columnas [id, fecha, tipo_de_evento, cantidad_fotos]
    a partir del mes y el año que toma la funcion
    2- Generar los datos a

    """
    





