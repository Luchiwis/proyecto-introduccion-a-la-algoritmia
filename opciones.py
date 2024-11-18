"""
Archivo con las funciones solicitadas en el documento
-Totales mes
-Total por tipo de EVENTO.
-Detalle por EVENTO.
-Detalle por día.
-Detalle del día.
"""

import datos
import fechas
import tablas
import operaciones


def totalesMes(eventos, mes, anio):
    totalFact = 0
    totalEventos = 0
    totalFotos = 0
    totalCosto = 0
    promedioFotosPorEvento = 0
    for evento in eventos:
        totalEventos += 1
        totalFact = totalFact + operaciones.facturar(evento)
        totalFotos = totalFotos + evento[5]
        totalCosto = totalCosto + operaciones.costo(evento)
    promedioFotosPorEvento = totalFotos / totalEventos

    #resultado
    print()
    print("*******************************************************")
    print(f"Mes: {fechas.queMes(mes)} del año {anio}")
    print(f"Total Facturado: ${totalFact}")
    print(f"Total Eventos Realizados: {totalEventos}")
    print(f"Total Fotos Realizadas: {totalFotos}")
    print(f"Total Costo Fotos Realizadas: ${totalCosto}")
    print(f"Promedio de fotos por evento es: {int(promedioFotosPorEvento)}")
    print("*******************************************************")
    print()


def totalPorTipoDeEvento(eventos, mes, anio):
    totalFact = 0
    totalEventos = 0
    totalFotos = 0
    totalCosto = 0
    promedioFotosPorEvento = 0
    print("Elija el tipo de evento (numero): ")
    print("1 - CASAMIENTO")
    print("2 - 15 AÑOS")
    print("3 - CUMPLEAÑOS")
    print("4 - BAUTISMOS")
    print("5 - OTROS")
    tipo = int(input())
    while tipo not in range(1,6):
        tipo = int(input("Ingrese un evento valido: "))
    TIPOS_DE_EVENTOS = [None, "CASAMIENTO", "QUINCE", "CUMPLE", "BAUTISMO", "OTRO"]
    eve = TIPOS_DE_EVENTOS[tipo]
    for evento in eventos:
        if evento[4] == eve:
            totalEventos += 1
            totalFact = totalFact + operaciones.facturar(evento)
            totalFotos = totalFotos + evento[5]
            totalCosto = totalCosto + operaciones.costo(evento)
    if totalEventos != 0:
        promedioFotosPorEvento = totalFotos / totalEventos
    else:
        promedioFotosPorEvento = 0

    #resultado
    print()
    print("*******************************************************")
    print(f"Mes: {fechas.queMes(mes)} del año {anio}")
    print(f"Tipo de Evento: {eve}")
    print(f"Total facturado: ${totalFact}")
    print(f"Total Eventos Realizados: {totalEventos}")
    print(f"Total Fotos Realizadas: {totalFotos}")
    print(f"Total Costo Fotos Realizadas: ${totalCosto}")
    print(f"Promedio de Fotos por Evento: {int(promedioFotosPorEvento)}")
    print("*******************************************************")
    print()


def detallePorEvento(eventos, mes, anio):
    """
    muestra todos los eventos del mes separados por tipo de evento y ordenados de menor a mayor facturacion
    """

    tabla = [["Tipo", "Total eventos", "Total fotos", "Total facturado"]]

    for tipo in ["CASAMIENTO", "QUINCE", "CUMPLE", "BAUTISMO", "OTRO"]:
        total_eventos_del_mes = 0
        total_fotos = 0
        total_facturado = 0
        for evento in eventos:
            if evento[4] == tipo:
                total_facturado += operaciones.facturar(evento)
                total_fotos += evento[5]
                total_eventos_del_mes += 1
        tabla.append([tipo, total_eventos_del_mes, total_fotos, total_facturado])

    # resultado
    print("Mes: ", fechas.queMes(mes), anio)
    tabla = tablas.ordenarTabla(tabla, 3) #ordenar por total facturado
    tabla = tablas.aplicarSignoPesos(tabla, 3)
    tablas.mostrarTabla(tabla)


def detallePorDia(eventos, mes, anio):
    """
    Esta funcion no utiliza tablas.ordenarTabla(). 
    Tiene su propio ordenamiento ya que lo que se comparan son fechas
    """
    
    tabla = []
    if mes == 2 and fechas.anioBisiesto(anio):
        diasMes = 29
    else:
        dias = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        diasMes = dias[mes]
        
    for i in range(diasMes):
        fecha = str(i + 1) + "/" + str(mes) + "/" + str(anio)
        dato = [fecha, 0, 0, 0]
        tabla.append(dato)
        
    for evento in eventos:
        dia = evento[1] - 1
        tabla[dia][1] += 1
        tabla[dia][2] += evento[5]
        tabla[dia][3] += operaciones.facturar(evento)

    # resultado
    print("Mes:", fechas.queMes(mes), anio)
    tabla = [["Día", "Total eventos", "Total fotos", "Total facturado"]] + tabla
    tabla = tablas.aplicarSignoPesos(tabla, 3)
    tablas.mostrarTabla(tabla)


def detalleDelDia(eventos, mes, anio):
    dia = int(input("ingrese un dia valido: "))
    while not fechas.validarFecha(dia, mes, anio):
        print(f"{dia}/{mes}/{anio} es una fecha invalida")
        dia = int(input("ingrese un dia valido: "))

    tabla = [["ID EVENTO", "Tipo de evento", "Total fotos", "Total facturado"]]
    for evento in eventos:
        if evento[1] == dia:
            tabla.append([evento[0], evento[4], evento[5], operaciones.facturar(evento)])

    #resultado
    print(f"Dia elegido: {dia} de {fechas.queMes(mes)} del año {anio}")
    tabla = tablas.ordenarTabla(tabla, 3) #ordenar por total facturado
    tabla = tablas.aplicarSignoPesos(tabla, 3)
    tablas.mostrarTabla(tabla)
