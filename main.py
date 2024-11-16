# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# -----------------            Programa principal        ----------------------------------
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
import datos
import opciones

def imprimirMenu():
    print()
    print("********************************************")
    print("Debe elegir una opcion, solo numeros enteros")
    print("1 - Totales mes")
    print("2 - Total por tipo de evento")
    print("3 - Detalle por evento")
    print("4 - Detalle por dia")
    print("5 - Detalle del dia")
    print("6 - SALIR")
    print("********************************************")
    print()


def main():
    mes = int(input("Ingrese el mes del que quiere saber los datos: "))
    while mes not in range(1, 13):
        mes = int(input("Ingrese un mes valido: "))

    anio = int(input("Ingrese el año del que quiere saber los datos: "))
        
    eventos = datos.generarEventos(mes, anio)
    imprimirMenu()

    op = int(input("Ingrese la opcion que desea: "))
    while op != 6:
        match op:
            case 1:
                opciones.totalesMes(eventos, mes, anio)
            case 2:
                opciones.totalPorTipoDeEvento(eventos, mes, anio)
            case 3:
                opciones.detallePorEvento(eventos, mes, anio)
            case 4:
                opciones.detallePorDia(eventos, mes, anio)
            case 5:
                opciones.detalleDelDia(eventos, mes, anio)
            case _:
                op = int(input("Opcion invalida, ingrese otra nuevamente: "))

        input("--Enter para continuar--")
        imprimirMenu()
        op = int(input("Ingrese otra opción: "))

    print("Fin del Programa")


main()
