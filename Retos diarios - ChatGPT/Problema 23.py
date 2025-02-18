"""
Problema 23: Verificar si dos listas son iguales (independientemente del orden y los duplicados)

Dada dos listas de enteros, escribe una función que verifique si contienen los mismos elementos, sin importar el orden ni la cantidad de veces que aparecen.

Instrucciones:

1.- La función debe recibir dos listas de enteros.
2.- Retorna True si contienen los mismos elementos (independientemente del orden y duplicados) y False en caso contrario.
"""

def verificar_listas(cadena1, cadena2): # Funcion que verifica si dos listas son iguales
    lista_enteros1 = set(map(int, cadena1.split())) # Convierte la cadena en un conjunto
    lista_enteros2 = set(map(int, cadena2.split())) # convierte la cadena en un conjunto
    
    return lista_enteros1 == lista_enteros2 # Retorna True si la comparacion sale positiva

#########################   Main    ################################

cadena1 = input("Ingrese la primera lista de números (separados por espacios): ")
cadena2 = input("Ingrese la segunda lista de números (separados por espacios): ")

if verificar_listas(cadena1, cadena2):
    print("Las listas son iguales.")
else:
    print("Las listas no son iguales.")