"""
Problema 2: Calcular el área de un círculo
Enunciado: Escribe un programa en Python que calcule el área de un círculo a partir del radio proporcionado por el usuario.

Requisitos:

Solicita al usuario que ingrese el radio del círculo.
1.- Usa la fórmula para calcular el área:
        Area = pi x radio**2    
2.- Usa el valor de pi que viene en la librería math.
3.- Muestra el resultado con dos decimales de precisión.
"""

import math # Importa el modulo math

radio = float(input("Ingrese el radio del circulo:")) # Solicita el radio de un circulo

area = math.pi * (radio**2) # Calcula el area de un circulo

print(f"El area del circulo ingresado es de: {round(area, 2)}") # Imprime el area del circulo y lo redondea a dos decimas