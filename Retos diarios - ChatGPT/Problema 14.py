"""
Problema 14: Encontrar el segundo número más grande
Enunciado: Escribe un programa en Python que reciba una lista de números enteros, encuentre el segundo número más grande de la lista y lo muestre.

Requisitos:

1.- El programa debe pedir al usuario que ingrese una lista de números separados por espacios.
2.- Debe encontrar el segundo número más grande.
3.- Si hay duplicados, estos deben ser ignorados para encontrar el segundo número más grande.
"""

def segundo_grande(cadena): # Funcion que encuentra el segundo numero mas grande
    lista_enteros = list(map(int, cadena.split()))  # Realiza un mapeo de la cadena dividida por espacios y las convierte a entero
    
    return sorted(set(lista_enteros))[-2] # Retorna la lista convirtiendola a conjunto para eliminar duplicados, la ordena ascendentemente y retorna el penultimo entero

#########################   Main    ################################

cadena = input("Ingrese una lista de enteros (separados por espacios):")

print(f"El segundo número mas grande es {segundo_grande(cadena)}.")