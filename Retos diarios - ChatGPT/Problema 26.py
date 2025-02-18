"""
Problema 26: Contar vocales en una cadena
Descripción: Escribe una función que cuente el número de vocales en una cadena 
de texto proporcionada por el usuario. La función debe ser insensible a mayúsculas y minúsculas.
"""

def contar_vocales(cadena): # Funcion que cuenta las vocales de una cadena
    vocales = set("aeiou") # Se inicializa un conjunto con las vocales
    suma = 0 # Se inicializa una suma para contar las vocales
    
    for letra in cadena.lower(): # Se itera sobre la cadena en minusculas
        if letra in vocales: # Si la letra esta en vocales
            suma += 1 # Agrega uno al contador
    
    return suma # Retorna la suma

#########################   Main    ################################

cadena = input("Ingrese una cadena de palabras: ")

print(f"La cantidad de vocales es: {contar_vocales(cadena)}")