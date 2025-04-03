"""
Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados.
"""

def sumar_ultimos(cadena): # Funcion que suma los 5 ultimos enteros ingresados
    lista_enteros = (list(map(int, cadena.split())))
    
    suma = 0
    for x in range(5,len(lista_enteros)):
        suma += lista_enteros[x]
    
    return suma

#########################   Main    ################################

enteros = input("Ingrese una lista de enteros (separados por espacios): ")

print(f"La suma de los ultimos 5 enteros ingresados es de {sumar_ultimos(enteros)}")