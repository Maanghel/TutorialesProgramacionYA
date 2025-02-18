"""
Problema 7: Verificar si un número es palíndromo
Enunciado: Escribe un programa en Python que verifique si un número entero ingresado por el usuario es un palíndromo. 
Un número es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda.

Requisitos:

1.- El programa debe pedir un número entero positivo al usuario.
2.- Debe verificar si el número es un palíndromo.
3.- Imprimir si el número es palíndromo o no.
"""

def verificar_palindromo(numero): # Funcion que verifica si un numero es palíndromo
    if numero < 0:  # Números negativos no son palíndromos
        return False 
    
    inversion = str(numero)[::-1] # convierte al numero en string para poder realizarle un slicing e invertirlo
    return inversion == str(numero) # Retorna True si el numero invertido y el numero convertido a string son iguales

#########################   Main    ################################

numero = int(input("Ingrese un número entero para verificar si es un palíndromo: "))

if verificar_palindromo(numero):
    print(f"El número {numero} es un palíndromo.")
else:
    print(f"El número {numero} no es un palíndromo.")