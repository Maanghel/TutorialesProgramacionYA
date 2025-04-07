"""
Crear un problema que implemente una funcion
de orden superior
"""

def operar(num1, num2, funcion):
    return funcion(num1, num2)

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return num1 // num2  

#########################   Main    ################################

print(f"La suma de 10 + 5 es {operar(10, 5, sumar)}")
print(f"La resta de 10 - 5 es {operar(10, 5, restar)}")
print(f"La multiplicacion de 10 * 5 es {operar(10, 5, multiplicar)}")
print(f"La division de 10 / 5 es {operar(10, 5, dividir)}")