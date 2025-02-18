"""
Problema 16: Encontrar el Máximo Común Divisor (MCD)
Escribe un programa en Python que reciba dos números enteros y devuelva su 
máximo común divisor (MCD). Utiliza el algoritmo de Euclides para resolver este problema.

Instrucciones:

1.- Define una función llamada calcular_mcd que tome dos números enteros como parámetros.
2.- Usa el algoritmo de Euclides para calcular el MCD.
3.- El programa debe solicitar al usuario que ingrese dos números enteros y luego llamar a la función para calcular y mostrar el MCD.
"""

def calcular_mcd(entero1, entero2): # Funcion que encuentra el MCD
    if entero2 == 0: # Si el entero2 llega a 0 se finaliza la funcion recursiva
        return entero1 # Retorna el entero1
	
    return calcular_mcd(entero2, entero1 % entero2) # Funcion recursiva 

#########################   Main    ################################

entero1 = int(input("Ingrese el primer número: "))
entero2 = int(input("Ingrese el segundo número: "))

print(f"El MCD de {entero1} y {entero2} es {calcular_mcd(entero1,entero2)}.")