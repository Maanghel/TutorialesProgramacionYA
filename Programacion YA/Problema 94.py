"""
Calcular el factorial de un número ingresado por teclado.
El factorial de un número es la cantidad que resulta de la multiplicación de determinado número natural por todos los números 
naturales que le anteceden excluyendo el cero. Por ejemplo el factorial de 4 es 24, que resulta de multiplicar 4*3*2*1.
No hay que implementar el algoritmo para calcular el factorial sino hay que importar dicha funcionalidad del módulo math.
El módulo math tiene una función llamada factorial que recibe como parámetro un entero del que necesitamos que nos retorne el factorial.
Solo importar la funcionalidad factorial del módulo math de la biblioteca estándar de Python.
"""

from math import factorial

entero = int(input("Ingrese un entero: "))
print(f"\nEl factorial de {entero} es: {factorial(entero)}") # Imprime el factorial de un entero por medio de la funcion factorial