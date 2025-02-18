"""
Problema 15: Números faltantes en un rango
Enunciado: Escribe un programa que reciba una lista de números enteros y luego determine 
cuáles números faltan en el rango entre el número mínimo y el número máximo de la lista.

Requisitos:

1.- El programa debe pedir al usuario que ingrese una lista de números separados por espacios.
2.- Debe calcular el rango entre el número mínimo y máximo de la lista.
3.- Mostrar los números que faltan en ese rango.
"""

def faltantes_enteros(cadena): # Funcion que retorna los numeros faltantes en un rango
    lista_enteros = list(map(int, cadena.split()))  # Realiza un mapeo de la cadena dividida por espacios y las convierte a entero
    rango_completo = set(range(min(lista_enteros), max(lista_enteros) + 1)) # Crea una variable en donde se crea un conjunto con un rango con el min y el max de la lista
    faltantes = rango_completo - set(lista_enteros) # Realiza una operacion entre conjuntos, dejando solo los numeros que faltaban
    
    return sorted(list(faltantes)) # Retorna los numeros faltantes ordenados ascendentemente

#########################   Main    ################################

cadena = input("Ingrese una lista de enteros (separados por espacios):")
lista_faltantes = faltantes_enteros(cadena)

print("\nLos números faltantes son:")
for numero in lista_faltantes:
    print(numero)