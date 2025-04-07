"""
Crear un problema que requiera el uso de una funcion lambda
para su solucion
"""

def operar(numero1, numero2, fn):
    return fn(numero1, numero2)

#########################   Main    ################################

print(f"La suma de 6 + 3 es de {operar(6, 3, lambda valor1, valor2: valor1 + valor2)}")
print(f"La resta de 6 - 3 es de {operar(6, 3, lambda valor1, valor2: valor1 - valor2)}")
print(f"La multiplicacion de 6 * 3 es de {operar(6, 3, lambda valor1, valor2: valor1 * valor2)}")
print(f"La division de 6 / 3 es de {operar(6, 3, lambda valor1, valor2: valor1 / valor2)}")