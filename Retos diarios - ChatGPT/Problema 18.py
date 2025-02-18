"""
Problema 18: Suma de múltiplos
Escribe una función que encuentre la suma de todos los múltiplos de 3 o 5 que sean menores que un número dado.
"""

def sumar_multiplos(entero): # Funcion que suma los multiplos de 3 y 5 que son menores a un numero dado
    numeros_multiplos = set([x for x in range(3, entero, 3)] + [x for x in range(5, entero, 5)]) # Compresion de lista para generar los multiplos
    
    return sum(numeros_multiplos) # Retorna la suma de los elementos de la lista

#########################   Main    ################################

entero = int(input("Ingrese un número entero: "))

print(f"La suma de los múltiplos de 3 o 5 menores que {entero} es {sumar_multiplos(entero)}") # Imprime la suma de los multiplos