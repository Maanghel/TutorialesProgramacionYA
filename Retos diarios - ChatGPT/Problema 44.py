"""
Problema 44: Lista Monotona
Escribe una función en Python que determine si una lista de enteros es monótona. Una lista es monótona si es completamente creciente o completamente decreciente.
"""

def es_monotona(lista): # Funcion que verifica si una lista es monotona
    creciente = True
    decreciente = True
    
    for i in range(1, len(lista)): # Itera sobre la lista para comprobar si es creciente o decreciente.
        if lista[i] < lista[i - 1]: # Verifica si el elemento actual de la lista es menor que el anterior
            creciente = False
        if lista[i] > lista[i - 1]: # Verifica que el elemento actual de la lista es mayor que el anterior
            decreciente = False
    
    return creciente or decreciente # Retorna True si creciente o decreciente sigue permaneciendo como True

#########################   Main    ################################

cadena = input("Ingrese una lista de enteros (separados por espacios): ")
lista_enteros = list(map(int, cadena.split()))

if es_monotona(lista_enteros):
    print("La lista es monótona.")
else:
    print("La lista no es monótona.")