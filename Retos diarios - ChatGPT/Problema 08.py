"""
Problema 8: Contador de palabras en una frase
Enunciado: Escribe un programa en Python que cuente cuántas palabras tiene una frase ingresada por el usuario. 
Una palabra es cualquier secuencia de caracteres separados por espacios.

Requisitos:

1.- El programa debe solicitar al usuario que ingrese una frase.
2.- Debe contar cuántas palabras hay en la frase y mostrar el resultado.
"""

def contar_palabras(cadena): # Funcion que cuenta las palabras de una cadena
    total_palabras = cadena.split()  # Divide la cadena en palabras
    
    return len(total_palabras)  # Retorna la cantidad de palabras en la lista

#########################   Main    ################################

cadena = input("Ingrese una cadena de palabras: ")

print(f"La frase tiene {contar_palabras(cadena)} palabras.")