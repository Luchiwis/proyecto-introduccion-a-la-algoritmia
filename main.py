# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# -----------------     Plantilla para diseño de un menú ----------------------------------
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
import utils
import datos
import opciones


def main():
    mes = int(input("Ingrese el mes del que quiere saber los datos: "))
    while mes not in range(1, 13):
        mes = int(input("Ingrese un mes valido: "))

    anio = int(input("Ingrese el año del que quiere saber los datos: "))
    eventos = datos.generarEventos(mes, anio)
    utils.imprimirMenu()
    
    op = int(input("Ingrese la opcion que desea: "))
    while op != 6:
        match op:
            case 1:
                opciones.totalesMes(eventos, mes, anio)
            case 2:
                opciones.totalPorTipoDeEvento(eventos,mes,anio,tipo)
            case 3:
                opciones.detalleEvento(eventos)
            case 4:
                opciones.detallePorDia(eventos)
            case 5:
                opciones.detalleDelDia(eventos)
                
            case _:
                op = int(input("Opcion invalida, ingrese otra nuevamente: "))

        input(":")
        utils.imprimirMenu()
        op = int(input("Ingrese otra opcion: "))

    print("Fin del Programa")


main()
