"""
Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares.
Emplear el operador “%” en la condición de la estructura condicional (este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):
	if valor%2==0:         
"""

def conteo_pares(cadena): # Funcion que retorna la cantidad de numeros pares e impares
    lista_enteros = list(map(int, cadena.split()))
    
    pares = 0
    impares = 0
    for entero in lista_enteros:
        if entero % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    return [pares, impares]

#########################   Main    ################################

cadena = input("Ingrese una lista de enteros (separados por espacios): ")

pares, impares = conteo_pares(cadena)

print(f"Cantidad de numeros pares: {pares}")
print(f"Cantidad de numeros impares: {impares}")