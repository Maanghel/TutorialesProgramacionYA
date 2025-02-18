"""
Problema 32: Contar palabras únicas
Escribe una función que tome una cadena de texto como entrada y devuelva el 
número de palabras únicas en esa cadena. Las palabras no deben diferenciar entre 
mayúsculas y minúsculas, y deben ignorarse los signos de puntuación.
"""

import re # Importa el modulo para expresiones regulares

def palabras_unicas(cadena): # Funcion que cuenta las palabras unicas
    cadena = re.sub(r'[^\w\s]', '', cadena) # Elimina todo lo que no sea palabra o espacio
    lista_palabras = cadena.lower().split() # Crea una lista de palabras en minusculas
    
    return set(lista_palabras) # Retorna un conjunto de palabras

#########################   Main    ################################

cadena = input("Ingrese una oracion: ")

print(f"{len(palabras_unicas(cadena))} (Las palabras únicas son: {palabras_unicas(cadena)})")