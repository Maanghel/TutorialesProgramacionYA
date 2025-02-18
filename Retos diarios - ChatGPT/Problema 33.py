"""
Problema 33: Contar la frecuencia de palabras en un texto
Escribe un programa que reciba una cadena de texto como entrada y cuente la frecuencia 
de cada palabra en esa cadena. El programa debe imprimir las palabras junto con su frecuencia.
"""

import re # Importa el modulo para expresiones regulares

def contar_frecuencias(cadena): # Funcion que cuenta la frecuencias de las palabras en una cadena
    frecuencias_palabras = {} # Inicializa un diccionario para la frecuencia
    
    cadena = re.sub(r'[^\w\s]', '', cadena) # Elimina todo lo que no sea palabras y espacios
    lista_palabras = cadena.lower().split() # Convierte en una lista de palabras
    
    for key in lista_palabras:
        if key in frecuencias_palabras: # Verifica si la palabra se encuentra en el diccionario
            frecuencias_palabras[key] += 1 # Suma 1 al value actual
        else:
            frecuencias_palabras[key] = 1 # Agrega una key con la palabra e inicializa el value en 1
    
    return frecuencias_palabras # Retorna el diccionario de frecuencia de palabras

#########################   Main    ################################

cadena = input("Ingrese una oracion: ")

diccionario_palabras = contar_frecuencias(cadena)

for x in diccionario_palabras: 
    print(f"{x}: {diccionario_palabras[x]}") # Imprime la key y value del diccionario