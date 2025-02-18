"""
Problema 11: Números perfectos
Enunciado: Un número perfecto es un número entero positivo que es igual a la suma de sus divisores 
propios (excluyendo el propio número). Por ejemplo, 6 es un número perfecto porque sus divisores propios son 1, 2 y 3, y 1 + 2 + 3 = 6.

Escribe un programa que determine si un número entero positivo es un número perfecto.

Requisitos:

1.- El programa debe pedir al usuario un número entero positivo.
2.- Calcular la suma de los divisores propios del número.
3.- Determinar si el número es perfecto o no, mostrando el resultado.
"""

def retornar_perfecto(entero): # Funcion que verifica si un numero es perfecto o no
    suma = 0
    for x in range(1, entero): # Itera desde el numero 1 hasta el numero ingresado
        if entero % x == 0:
            suma += x  # Suma los divisores directamente
    
    return suma == entero  # Retorna True si es perfecto, False en caso contrario

#########################   Main    ################################

entero = int(input("Ingrese un número entero para verificar si es perfecto o no: "))

if retornar_perfecto(entero):
    print(f"El número {entero} es un número perfecto.")
else:
    print(f"El número {entero} no es un número perfecto.")