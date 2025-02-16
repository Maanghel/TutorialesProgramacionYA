"""
Cargar una lista con 5 elementos enteros. Ordenarla de menor a mayor y
mostrarla por pantalla. luego ordenar de mayor a menor e imprimir nuevamente.
"""

# Funcion que ordena la lista de menor a mayor
def ordenar_menor_mayor(enteros):
    for x in range(4):
        for y in range(4):
            if enteros[y] > enteros[y+1]:
                aux = enteros[y]
                enteros[y] = enteros[y+1]
                enteros[y+1] = aux
    
    return enteros

    # Mediante la funcion sorted podemos ordenar la lista igualmente
    # return sorted(enteros)

# Funcion que ordena la lista de mayor a menor
def ordenar_mayor_menor(enteros): 
    for x in range(4):
        for y in range(4):
            if enteros[y] < enteros[y+1]:
                aux = enteros[y]
                enteros[y] = enteros[y+1]
                enteros[y+1] = aux
    
    return enteros
    
    # Mediante la funcion sorted podemos ordenar la lista de mayor a menor
    # return sorted(enteros, reverse=True)

#########################   Main    ################################

lista = [3, 2, 5, 1, 4]

print(f"Lista ordenada de menor a mayor: \n{ordenar_menor_mayor(lista)}")

print(f"\nLista ordenada de mayor a menor: \n{ordenar_mayor_menor(lista)}")