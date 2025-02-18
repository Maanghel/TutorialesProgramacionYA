"""
Problema 5: Revertir una cadena de texto
Enunciado: Escribe un programa en Python que solicite una cadena de texto (palabra o frase) y devuelva la cadena invertida.

Requisitos:

1.- El programa debe pedir al usuario que ingrese una palabra o frase.
2.- Debe imprimir la cadena en orden inverso (sin cambiar las letras mayúsculas o minúsculas).
3.- No puedes usar funciones predefinidas como reversed().
"""

def retornar_invertido(cadena): # Funcion que retorna la cadena invertida
    inversion = cadena[::-1] # Realiza un slicing para invertir la cadena
    
    return inversion # Retorna la cadena invertida

#########################   Main    ################################

cadena = input("Ingrese una cadena de texto para invertirla: ")

print(f"\nLa cadena invertida es: {retornar_invertido(cadena)}")