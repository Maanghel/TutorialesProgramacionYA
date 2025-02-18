"""
Problema 21: Verificar Pangrama
Escribe un programa que determine si una cadena de texto es un pangrama o no. 
Un pangrama es una oración que contiene todas las letras del alfabeto al menos una vez.
"""

def verificar_pangrama(cadena): # Funcion que verifica si la oracion es un pangrama
    abecedario = set("abcdefghijklmnopqrstuvwxyz") # Creamos un conjunto con las letras del abecedario
    
    letras_cadena = set(cadena.lower()) # Convierte en conjunto la cadena hecha minuscula
    
    if abecedario.issubset(letras_cadena): # Verifica si el abecedario es un subconjunto de la lista
        return True
    else:
        return False

#########################   Main    ################################

cadena = input("Ingrese una cadena de texto: ")

if verificar_pangrama(cadena):
    print("La cadena es un pangrama.")
else:
    print("La cadena no es un pangrama.")