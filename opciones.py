"""
Archivo con las funciones solicitadas en el documento
-Totales mes
-Total por tipo de EVENTO.
-Detalle por EVENTO.
-Detalle por día.
-Detalle del día.
"""

import utils
import datos


def totalesMes(eventos, mes, anio):
    totalFact = 0
    totalEventos = 0
    totalFotos = 0
    totalCosto = 0
    promedioFotosPorEvento = 0
    for evento in eventos:
        totalEventos += 1
        totalFact = totalFact + datos.facturar(evento)
        totalFotos = totalFotos + evento[5]
        totalCosto = totalCosto + datos.costo(evento)
    promedioFotosPorEvento = totalFotos / totalEventos

    #resultado
    print()
    print("*******************************************************")
    print(f"Mes: {utils.queMes(mes)} del año {anio}")
    print("Total Facturado: $", totalFact)
    print("Total Eventos Realizados: ", totalEventos)
    print("Total Fotos Realizadas: ", totalFotos)
    print("Total Costo Fotos Realizadas: ", totalCosto)
    print("Promedio de fotos por evento es: ", promedioFotosPorEvento)
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
            totalFact = totalFact + datos.facturar(evento)
            totalFotos = totalFotos + evento[5]
            totalCosto = totalCosto + datos.costo(evento)
    if totalEventos != 0:
        promedioFotosPorEvento = totalFotos / totalEventos
    else:
        promedioFotosPorEvento = 0

    #resultado
    print()
    print("*******************************************************")
    print(f"Mes: {utils.queMes(mes)} del año {anio}")
    print("Tipo de Evento: ", eve)
    print("Total facturado: $", totalFact)
    print("Total Eventos Realizados: ", totalEventos)
    print("Total Fotos Realizadas: ", totalFotos)
    print("Total Costo Fotos Realizadas: ", totalCosto)
    print("Promedio de Fotos por Evento: ", promedioFotosPorEvento)
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
                total_facturado += datos.facturar(evento)
                total_fotos += evento[5]
                total_eventos_del_mes += 1
        tabla.append([tipo, total_eventos_del_mes, total_fotos, total_facturado])

    # resultado
    print("Mes: ", utils.queMes(mes), anio)
    tabla = utils.ordenarTabla(tabla, 3) #ordenar por total facturado
    utils.mostrarTabla(tabla)


def detallePorDia(eventos, mes, anio):
    """
    Esta funcion no utiliza utils.ordenarTabla(). 
    Tiene su propio ordenamiento ya que lo que se comparan son fechas
    """
    
    tabla = []
    if mes == 2 and utils.anioBisiesto(anio):
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
        tabla[dia][3] += datos.facturar(evento)

    # resultado
    print("Mes:", utils.queMes(mes), anio)
    tabla = [["Día", "Total eventos", "Total fotos", "Total facturado"]] + tabla
    # print(tabla)
    utils.mostrarTabla(tabla)


def detalleDelDia(eventos, mes, anio):
    dia = int(input("ingrese un dia valido: "))
    while not utils.validarFecha(dia, mes, anio):
        print(f"{dia}/{mes}/{anio} es una fecha invalida")
        dia = int(input("ingrese un dia valido: "))

    tabla = [["ID EVENTO", "Tipo de evento", "Total fotos", "Total facturado"]]
    for evento in eventos:
        if evento[1] == dia:
            tabla.append([evento[0], evento[4], evento[5], datos.facturar(evento)])

    #resultado
    print(f"Dia elegido: {dia} de {utils.queMes(mes)} del año {anio}")
    tabla = utils.ordenarTabla(tabla, 0) #ordenar por total facturado
    utils.mostrarTabla(tabla)

if __name__ == "__main__":
    d = datos.generarEventos(1, 2020)
    print(d)
    detallePorDia(d, 1, 2020)
