"""
Problema 1: Determinar si un número es par o impar
Enunciado: Escribe un programa en Python que pida al usuario que ingrese un número y determine si el número es par o impar.

Requisitos:

El programa debe solicitar un número entero al usuario.
1.- Debe imprimir "El número es par" si el número es divisible por 2 sin dejar resto.
2.- Debe imprimir "El número es impar" si el número no es divisible por 2.
"""

num = int(input("Introduzca un número: "))

# Verifica si el residuo es 0 para identificar si es par
if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")