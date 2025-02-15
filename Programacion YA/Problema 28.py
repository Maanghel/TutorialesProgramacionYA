"""
Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la tabla de multiplicar del mismo (los primeros 12 términos)
Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9, hasta el 36.
"""

def imprimir_tabla(entero): # Funcion que imprime una tabla de multiplicar del numero especificado
    for x in range(1, 13):
        print(entero * x)

#########################   Main    ################################

numero = int(input("Ingrese un numero del 1 al 10 del cual quiera imprimir una tabla de multiplicar con los 12 primeros terminos: "))

imprimir_tabla(numero)