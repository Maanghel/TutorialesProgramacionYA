"""
Problema #30: Numeros Unicos
Crea una función que reciba dos listas de números enteros. La función debe devolver 
una nueva lista que contenga solo los números que son únicos en ambas listas (es decir, 
números que aparecen solo en una de las listas, pero no en ambas).
"""

def numeros_unicos(cadena1, cadena2): # Funcion que retorna una lista con los numeros unicos
    lista_enteros1 = set(map(int,cadena1.split())) # Convierte en un conjunto a la cadena de enteros
    lista_enteros2 = set(map(int,cadena2.split())) # Convierte en un conjunto a la cadena de enteros
    numeros_unicos = list(lista_enteros1 ^ lista_enteros2) # Usa el operador de comparacion para conseguir una lista con los numeros unicos
    
    return numeros_unicos # Retorna la lista con los numeros unicos

#########################   Main    ################################

cadena1 = input("Ingrese la primer lista de números enteros (separados por espacios): ")
cadena2 = input("Ingrese la segundo lista de números enteros (separados por espacios): ")

print(f"Numeros unicos de las dos listas: {numeros_unicos(cadena1, cadena2)}")