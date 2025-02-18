"""
Problema 20: Secuencia creciente
Escribe un programa que acepte una lista de números enteros y determine si esos números están en una secuencia creciente o no.
"""

def retornar_creciente(cadena): # Funcion que verifica si una cadena de enteros es creciente o no
    lista_enteros = list(map(int,cadena.split())) # Realiza un mapeo de la cadena dividida por espacios y las convierte a entero
    
    if lista_enteros == sorted(lista_enteros): # Si la lista de enteros es igual a la misma lista ordenada, retorna True
        return True
    else:
        return False

#########################   Main    ################################

cadena = input("Ingrese una lista de números enteros (separados por espacios): ")

if retornar_creciente(cadena):
    print("La lista esta en un orden creciente.")
else:
    print("La lista no esta en un orden creciente.")