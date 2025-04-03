"""
Realizar un programa que solicite la carga por teclado de dos números, 
si el primero es mayor al segundo informar su suma y diferencia, en caso 
contrario informar el producto y la división del primero respecto al segundo.
"""

def mayor_menor(entero1, entero2): # Funcion que retorna una operacion segun cual entero sea mayor
    if entero1 >= entero2:
        return [entero1 + entero2, entero1 - entero2]
    else:
        return [entero1 * entero2, entero1 / entero2]

#########################   Main    ################################

numero1 = int(input("Ingrese el primer entero: "))
numero2 = int(input("Ingrese el segundo entero: "))

if numero1 >= numero2:
    print(f"La suma es: {mayor_menor(numero1, numero2)[0]} - La diferencia es: {mayor_menor(numero1, numero2)[1]}")
else:
    print(f"El producto es: {mayor_menor(numero1, numero2)[0]} - La division es: {mayor_menor(numero1, numero2)[1]}")