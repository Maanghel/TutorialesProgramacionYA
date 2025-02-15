"""
Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde a Navidad.
"""

def imprimir_navidad(dia, mes): # Funcion que te indica si la fecha corresponde a navidad
    if dia == 25 and mes == 12:
        print("Es navidad.")
    else:
        print("No es navidad.")

#########################   Main    ################################

dia = int(input("Ingrese el dia del mes: "))
mes = int(input("Ingrese el numero del mes: "))

imprimir_navidad(dia, mes,)