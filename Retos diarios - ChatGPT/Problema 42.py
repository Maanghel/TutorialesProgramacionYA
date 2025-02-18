"""
Problema 42: Anagramas
Escribe una función en Python que determine si una cadena es un anagrama de otra. 
Un anagrama es una palabra o frase que resulta de reorganizar las letras de otra 
palabra o frase, usando todas las letras una sola vez.
"""

import re

def verificar_anagrama(cadena1, cadena2): # Funcion para verificar si dos cadenas son anagramas
    cadena1_limpia = re.sub(r'[\W_]', '', cadena1.lower()) # Elimina todo excepto los numeros y letras
    cadena2_limpia = re.sub(r'[\W_]', '', cadena2.lower()) # Elimina todo excepto los numeros y letras
    
    return sorted(cadena1_limpia) == sorted(cadena2_limpia) # Compara las dos cadenas acomodadas

#########################   Main    ################################

cadena1 = input("Ingrese una palabra o frase: ")
cadena2 = input("Ingrese una segunda palabra o frase: ")

if verificar_anagrama(cadena1, cadena2):
    print("Las cadenas son anagramas.")
else:
    print("Las cadenas no son anagramas.")