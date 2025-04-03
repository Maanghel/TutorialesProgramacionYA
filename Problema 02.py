"""
Escribir un programa en el cual se ingresen cuatro números, calcular e 
informar la suma de los dos primeros y el producto del tercero y el cuarto.
"""

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))
numero4 = int(input("Ingrese el cuarto numero: "))

suma = numero1 + numero2
producto = numero3 * numero4

print(f"La suma de los dos primeros es: {suma}")
print(f"El producto de los dos ultimos es: {producto}")