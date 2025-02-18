"""
Problema 6: Números primos
Enunciado: Escribe un programa en Python que determine si un número ingresado por el usuario es un número primo.

Requisitos:

1.- El programa debe pedir un número entero positivo al usuario.
2.- Verifica si el número es primo (un número es primo si solo es divisible por 1 y por sí mismo).
3.- El programa debe imprimir si el número es primo o no.
"""

def verificar_primo(numero): # Funcion que verifica si un numero es primo
    if numero < 2:  # Los números menores a 2 no son primos
        return False
    
    for x in range(2, numero): # Itera desde el 2 hasta el numero ingresado buscando un divisor exacto
        if numero % x == 0: # Si el residuo es 0 retorna Falso
            return False
    
    return True # Retorna True

#########################   Main    ################################

numero = int(input("Ingrese un número entero: "))
primo = verificar_primo(numero)

if primo:
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")