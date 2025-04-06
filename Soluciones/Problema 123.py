"""
Crear un problema que requiera la implementacion de una solucion
recursiva
"""

def fibonacci(numero1= 1, numero2= 2, sum_fibonacci = 0):
    if numero2 >= 4000000:
        return sum_fibonacci
    elif numero2 % 2 == 0:
        sum_fibonacci += numero2
    
    return fibonacci(numero1= numero2, numero2= numero1 + numero2, sum_fibonacci= sum_fibonacci)

#########################   Main    ################################

print(fibonacci())