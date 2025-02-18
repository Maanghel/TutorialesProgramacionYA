"""
Problema 13: Calcular la suma de los números pares de una lista
Enunciado: Escribe un programa en Python que reciba una lista de números enteros y calcule la suma de todos los números pares en la lista.

Requisitos:

1.- El programa debe pedir al usuario que ingrese una lista de números separados por espacios.
2.- Debe calcular la suma de los números pares.
3.- Mostrar la suma total al usuario.
"""

def sumar_pares(cadena): # Funcion que suma los numeros pares de una lista
    lista_enteros = list(map(int, cadena.split()))  # Realiza un mapeo de la cadena dividida por espacios y las convierte a enteros
    
    suma = 0
    for entero in lista_enteros: # Itera sobre la lista
        if entero % 2 == 0: # Verifica si es par
            suma += entero # En caso de True suma el entero
    
    return suma # Retorna la suma

#########################   Main    ################################

cadena = input("Ingrese una lista de enteros (separados por espacios):")

print(f"La suma de los números pares es {sumar_pares(cadena)}.")