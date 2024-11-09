# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# -----------------     Plantilla para diseño de un menú ----------------------------------
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
import utils


# Funciones


# Funcion que imprime el menu por pantalla
# Se agregan las opciones necesarias segun el programa de cada uno.
def imprimirMenu():
    while True:
        print()
        print("********************************************")
        print("Debe elegir una opcion, solo numeros enteros")
        print("1 - Totales mes")
        print("2 - Total por tipo de EVENTO")
        print("3 - Detalle por EVENTO")
        print("4 - Detalle por mes")
        print("5 - Detalle del día")
        print("6 - Salir")
        print("********************************************")
        print()

        return 

# Funcion que valida que las opciones elegidas del menu sean las correctas.
# Solo valida numeros. Si se ingresa letras se corta el programa.
# Agregar las opciones necesarias segun el programa de cada uno.


def validarOpcionMenu(opcion):
    if utils.elementoEnLista(
        opcion, [1, 2, 3, 4, 5, 6]
    ):  # Se ha ingresado un valor invalido por menu
        return True
    else:
        return False


# ************************
# Programa principal
# ************************


print("Bienvenido al programa")
print()

# Leer la primera vez la opcion del menu

opcion = imprimirMenu()

# Comienzo del proceso de las opciones del menu elegidas.

while opcion != 0:

    flagMenu = validarOpcionMenu(opcion)
    while flagMenu == False:
        print("Opcion de menu invalida, vuelva a ingresar...")
        print()
        opcion = int(input("Ingrese la opcion elegida del menu principal: "))
        flagMenu = validarOpcionMenu(opcion)

    # Analizamos las opciones validas del menú
    if opcion == 1:
        # Instrucciones para la opcion 1
        print("Has elegido la opcion 1")
        # ingreso de datos para opcion 1
        # proceso de datos para opcion 1
        # impresion de datos para opcion 1
    elif opcion == 2:
        print("Has elegido la opcion 2")
        # ingreso de datos para opcion 2
        # proceso de datos para opcion 2
        # impresion de datos para opcion 2
    elif opcion == 3:
        print("Has elegido la opcion 3")
        # ingreso de datos para opcion 3
        # proceso de datos para opcion 3
        # impresion de datos para opcion 3

    # Luego de procesar la opcion del menu elegida
    # Vuelvo a invocar al menu
    imprimirMenu()
    opcion = int(input("Ingrese la opcion elegida del menu principal: "))

else:
    print("FIN DEL PROGRAMA")


# Fin del programa
