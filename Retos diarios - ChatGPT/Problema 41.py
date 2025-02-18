"""
Problema #41: Invertir las palabras de una cadena

Escribe una función que tome una cadena de texto como entrada y 
devuelva una nueva cadena en la que el orden de las palabras esté invertido, 
pero el orden de las letras en cada palabra permanezca igual.
"""

def invertir_cadena(cadena): # Funcion que retorna la cadena invertida
    return " ".join(cadena.split()[::-1]) # Retorna la cadena invertida y separada por espacios

#########################   Main    ################################

cadena = input("Ingrese una cadena de palabras para invertirla: ")

print(f"La cadena invertida es:\n{invertir_cadena(cadena)}")