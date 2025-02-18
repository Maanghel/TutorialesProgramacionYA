"""
Problema 34: Verificar Palíndromos
Escribe una función que determine si una frase es un palíndromo. 
Un palíndromo es una palabra o frase que se lee igual de izquierda a derecha y de derecha a 
izquierda, ignorando espacios, mayúsculas, minúsculas y signos de puntuación.
"""

import re # Importa el modulo para expresiones regulares

def verificar_palindromo(cadena): # Funcion que verifica si una frase es un palindromo
    cadena_limpia = re.sub(r'[\W_]', '', cadena.lower())  # Elimina todo lo que no es letra o número
    
    return cadena_limpia == cadena_limpia[::-1]  # Compara directamente la cadena con su inversa

#########################   Main    ################################

cadena = input("Ingrese una palabra o frase para verificar si es un palindromo: ")

if verificar_palindromo(cadena):
    print("La frase es un palindromo.")
else:
    print("La frase no es un palindromo.")