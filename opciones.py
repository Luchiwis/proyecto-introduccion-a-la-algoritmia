import utils
import datos


def totalesMes(eventos, mes, anio):
    mes = utils.queMes(mes)
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

    print()
    print("*******************************************************")
    print("Mes:", mes, anio)
    print("Total Facturado: $", totalFact)
    print("Total Eventos Realizados: ", totalEventos)
    print("Total Fotos Realizadas: ", totalFotos)
    print("Total Costo Fotos Realizadas: ", totalCosto)
    print("Promedio de fotos por evento es: ", promedioFotosPorEvento)
    print("*******************************************************")
    print()


def totalPorTipoDeEvento(eventos, mes, anio):
    mes = utils.queMes(mes)
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
    while tipo < 1 or tipo > 5:
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

    print("Tipo de Evento: ", eve)
    print("Total facturado: ", totalFact)
    print("Total Eventos Realizados: ", totalEventos)
    print("Total Fotos Realizadas", totalFotos)
    print("Total Costo Fotos Realizadas: ", totalCosto)
    print("Promedio de Fotos por Evento", promedioFotosPorEvento)


def detallePorEvento(eventos, mes, anio):
    
    filas = []
    for tipo in ["CASAMIENTO", "QUINCE", "CUMPLE", "BAUTISMO", "OTRO"]:
        total_eventos_del_mes = 0
        total_fotos = 0
        total_facturadoo = 0
        for evento in eventos:
            if evento[4] == tipo:
                total_facturadoo += datos.facturar(evento)
                total_fotos += evento[5]
                total_eventos_del_mes += 1
        filas.append([evento, total_eventos_del_mes, total_fotos, total_facturadoo])
    print(f"{'dia':<20}", f"{'Total eventos':<20}", f"{'Total fotos':<20}", f"{'Total facturado':<20}")
        # print(f"{tipo:<20}", f"{total_eventos_del_mes:<22}", f"{total_fotos:<20}", f"{total_facturadoo:<20}")


def detallePorDia(eventos, mes, anio):
    rta = []
    bis = datos.anioBisiesto(anio)
    if mes == 2 and bis:
        diasMes = 29
    else:
        dias = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        diasMes = dias[mes]
    i = 0
    while i < diasMes:
        fecha = str(i+1)+"/"+str(mes)+"/"+str(anio)
        dato = [fecha, 0, 0, 0]
        rta.append(dato)
        i += 1
    for evento in eventos:
        dia = evento[1]-1
        rta[dia][1] += 1
        rta[dia][2] += evento[5]
        rta[dia][3] += datos.facturar(evento)
    for i in range(len(rta)):
        print(rta[i])


    


def detalleDelDia(eventos):
    pass


if __name__ == "__main__":
    d = datos.generarEventos(1, 2020)
    print(d)
    detallePorDia(d, 1, 2020)
