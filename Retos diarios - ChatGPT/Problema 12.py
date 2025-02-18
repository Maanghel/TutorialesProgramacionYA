"""
Problema 12: Encontrar el número más grande en una lista
Enunciado: Escribe un programa en Python que reciba una lista de números enteros y encuentre el número más grande de la lista.

Requisitos:

1.- El programa debe pedir al usuario que ingrese una lista de números separados por espacios.
2.- Debe encontrar el número más grande de la lista.
3.- Mostrar el número más grande al usuario.
"""

def retornar_mayor(cadena): # Funcion que encuentra el numero mas grande de una lista
    numeros_enteros = list(map(int, cadena.split()))  # Realiza un mapeo de la cadena dividida por espacios y las convierte a enteros
    
    return max(numeros_enteros) # Retorna el maximo de la lista por medio de la funcion max

#########################   Main    ################################

cadena = input("Introduzca una lista de números enteros (separados por espacios): ")

print(f"El número más grande es {retornar_mayor(cadena)}.")