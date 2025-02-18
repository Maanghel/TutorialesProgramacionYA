"""
Problema 45: Contar dígitos pares en un número
Dado un número entero positivo, escribe una función en Python que cuente cuántos 
dígitos pares contiene. Por ejemplo, si el número es 2485, la función debe retornar 3 (porque 2, 4 y 8 son pares).
"""

def contar_pares(numero): # Funcion que cuenta los digitos pares de un entero
    return sum(1 for digito in numero if int(digito) % 2 == 0) # Se usa la funcion sum y compresion de lista para contabilizar el total de digitos pares

#########################   Main    ################################

numero = input("Ingrese un entero: ")

print(f"El total de números pares en el valor ingresado es: {contar_pares(numero)}")