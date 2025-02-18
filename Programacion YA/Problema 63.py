"""
Desarrollar un programa que solicite la carga de tres valores y muestre el menor. 
Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)
"""

# Funcion que solicita 3 enteros y devuelve el menor de ellos
def mostar_menor():
    entero1 = int(input("\nIngrese el primer entero: "))
    entero2 = int(input("Ingrese el segundo entero: "))
    entero3 = int(input("Ingrese el tercer entero: "))
    
    print(min(entero1, entero2, entero3))

#########################   Main    ################################

mostar_menor()
mostar_menor()