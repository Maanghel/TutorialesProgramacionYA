"""
Problema 10: Contar números pares e impares en una lista
Enunciado: Escribe un programa en Python que reciba una lista de números enteros del usuario y cuente cuántos números son pares y cuántos son impares.

Requisitos:

1.- El programa debe pedir una lista de números enteros al usuario (puedes pedir que los ingrese separados por espacios).
2.- Debe contar cuántos números son pares y cuántos son impares.
3.- Mostrar ambos resultados al usuario.
"""

def retornar_paresimpares(enteros): # Funcion que cuenta los numeros pares e impares
    pares = 0
    impares = 0
    total_enteros = enteros.split() # Divide la lista ingresada y separada por espacios
    
    for numero in total_enteros: # Itera sobre la lista
        if int(numero) % 2 == 0: # convierte el numero en entero y lo divide entre dos para verificar si es par
            pares += 1
        else:
            impares += 1
    
    return [pares, impares] # Retorna una lista con dos componentes tipo lista

#########################   Main    ################################

enteros = input("Ingrese una lista de números (separados por espacios): ")

pares, impares = retornar_paresimpares(enteros) # Realiza una asignacion doble
print(f"Hay {pares} números pares y {impares} números impares.")