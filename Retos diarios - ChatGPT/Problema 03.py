"""
Problema 3: Conversión de grados Celsius a Fahrenheit
Enunciado: Escribe un programa en Python que convierta una temperatura dada en grados Celsius a grados Fahrenheit.

Requisitos:

El programa debe solicitar al usuario que ingrese la temperatura en grados Celsius.
1.- Usa la fórmula para convertir de Celsius a Fahrenheit:
        F = 9/5 x C + 32
2.- El programa debe mostrar el resultado redondeado a 2 decimales.
"""

def retornar_fahrenheit(grados): # Funcion que retorna los grados Celcius en Fahrenheit
    fah = (9/5 * grados) + 32 # Operacion para convertir Celsius en Fahrenheit
    
    return fah # Retorna la variable fah

#########################   Main    ################################

grados = float(input("Ingrese los grados Celsius que quiere convertir a Fahrenheit: "))

print(f"La conversión de {grados} grados Celsius es {round(retornar_fahrenheit(grados), 2)} grados Fahrenheit.") # Imprime los grados fahrenheit y lo redondea a 2 decimas