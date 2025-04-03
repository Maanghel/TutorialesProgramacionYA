"""
Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos.
"""

def mostrar_mayor(entero1,entero2,entero3): # Funcion que retorna el maximo de una serie de tres numeros
    return max(entero1,entero2,entero3) # Retorna el maximo de los enteros usando la funcion max

#########################   Main    ################################

entero1 = int(input("Ingrese el primer entero: "))
entero2 = int(input("Ingrese el segundo entero: "))
entero3 = int(input("Ingrese el tercer entero: "))

print(f"El mayor de los numeros ingresados es: {mostrar_mayor(entero1, entero2, entero3)}")