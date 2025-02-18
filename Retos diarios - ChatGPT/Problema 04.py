"""
Problema 4: Contar vocales en una palabra
Enunciado: Escribe un programa en Python que solicite una palabra al usuario y cuente cuántas vocales contiene.

Requisitos:

1.- El programa debe pedir al usuario que ingrese una palabra.
2.- Debe contar las vocales (a, e, i, o, u) tanto mayúsculas como minúsculas.
3.- Mostrar el número total de vocales encontradas.
"""

def mostrar_vocales(palabra): # Funcion que cuenta las vocales en una palabra
    palabra = palabra.lower()  # Convertimos toda la palabra a minúsculas de una vez
    
    contador = 0
    for letra in palabra: # Itera sobre la palabra letra a letra
        if letra in "aeiou":  # Verificamos si la letra está entre las vocales
            contador += 1
    
    print(f"La cantidad de vocales que tiene la palabra es: {contador}")

#########################   Main    ################################

palabra = input("Ingrese una palabra para contar sus vocales: ")

mostrar_vocales(palabra)