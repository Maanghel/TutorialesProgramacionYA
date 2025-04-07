"""
Codificar un programa que muestre en pantalla los números del 1 al 100, 
sustituyendo los múltiplos de 3 por el palabra "Fizz" y, a su vez, los múltiplos de 
5 por "Buzz". Para los números que, al tiempo, son múltiplos de 3 y 5, mostrar el mensaje "FizzBuzz".
"""

print(["Fizz" * (not numero % 3) + "Buzz" * (not numero % 5) or numero for numero in range(1, 101)])