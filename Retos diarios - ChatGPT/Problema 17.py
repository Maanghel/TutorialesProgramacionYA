"""
Problema 17: Números amigos
Dos números son llamados números amigos si la suma de los divisores propios 
de uno es igual al otro, y viceversa. Por ejemplo, 220 y 284 son números amigos, ya que:

Los divisores propios de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, y 110, y su suma es 284.
Los divisores propios de 284 son 1, 2, 4, 71, y 142, y su suma es 220.
"""

def numeros_amigos(entero): # Funcion que verifica si dos numeros son amigos
    numeros_propios = [x for x in range(1, entero) if entero % x == 0] # Compresion de lista
    
    return sum(numeros_propios) # Retorna la suma de los enteros en al lista y suma sus elementos con la funcion sum

#########################   Main    ################################

entero1 = int(input("Ingrese el primer número: "))
entero2 = int(input("Ingrese el segundo número: "))

if numeros_amigos(entero1) == entero2 and numeros_amigos(entero2) == entero1: # Verifica que sean numeros amigos
    print(f"{entero1} y {entero2} son números amigos.")
else:
    print(f"{entero1} y {entero2} no son números amigos.")