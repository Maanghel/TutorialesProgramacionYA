"""
Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar un mensaje indicando si el número tiene uno o dos dígitos.
(Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)
"""

def verificar_digitos(numero): # Funcion que verifica si el numero tiene 1 o 2 digitos
    if numero >= 10 and numero < 100:
        print("El numero tiene dos digitos.")
    elif numero > 0 and numero < 10:
        print("El numero tiene un digito.")
    else:
        print("Ingrese un numero valido.")

#########################   Main    ################################

numero = int(input("Ingrese un numero de uno o dos digitos: "))

verificar_digitos(numero)