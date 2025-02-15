"""
Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc. (No se ingresan valores por teclado)
"""

def imprimir_terminos(): # Funcion que imprime 25 terminos de la serie 11
    for x in range(1, 26):
        print(11 * x, sep = "-",end = " ")

#########################   Main    ################################

imprimir_terminos()