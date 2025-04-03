"""
Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16 - 24, etc.
"""

def mostrar_multiplos(entero = 8): # Funcion que muestra los multiplos de 8
    for x in range(8, 500, 8):
        print(x, end=" ")

#########################   Main    ################################

mostrar_multiplos()