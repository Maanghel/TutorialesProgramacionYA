"""
Problema 38: Calcular el MCD
Escribe una función que tome dos números enteros como entrada y devuelva el máximo común divisor (MCD) de los dos números.
"""

import math # Importa el modulo math para operaciones matematicas

def calcular_mcd(entero1, entero2): # Funcion que retorna el MCD de dos numeros
    return math.gcd(entero1, entero2) # Usamos la funcion gcd del modulo math para retornar el MCD 

#########################   Main    ################################

entero1 = int(input("Ingrese el primer número: "))
entero2 = int(input("Ingrese el segundo número: "))

print(f"El MCD de {entero1} y {entero2} es: {calcular_mcd(entero1, entero2)}")