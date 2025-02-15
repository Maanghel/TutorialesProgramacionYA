"""
Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras
y muestre un mensaje indicando si tiene 1, 2, o 3 cifras. Mostrar un mensaje de error si el número de cifras es mayor.
"""

def mostrar_cifras(entero): # Funcion que indica la cantidad de cifras que tiene el entero
    if entero < 10 and entero > 0:
        print("El numero tiene una cifra.")
    elif entero < 100 and entero >= 10:
        print("El numero tiene dos cifras.")
    elif entero < 1000 and entero >= 100:
        print("El numero tiene tres cifras.")
    else:
        print("Ingrese un numero valido.")

#########################   Main    ################################

entero = int(input("Ingrese un numero (entre una y tres cifras): "))

mostrar_cifras(entero)