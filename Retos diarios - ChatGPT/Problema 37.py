"""
Problema 37: Calcular el MCM de dos números
Escribe una función en Python que tome dos números enteros y calcule el Mínimo Común Múltiplo (MCM) de ambos.
"""

import math # Importa el modulo math para operaciones matematicas

def calcular_mcm(entero1, entero2): # Funcion que retorna el MCM de dos numeros
    mcm = (entero1 * entero2) // math.gcd(entero1, entero2) # Formula para obtener el MCM de dos numeros
    
    return mcm # Retorna el MCM

#########################   Main    ################################

entero1 = int(input("Ingrese el primer número: "))
entero2 = int(input("Ingrese el segundo número: "))

print(f"El MCM de {entero1} y {entero2} es: {calcular_mcm(entero1, entero2)}")