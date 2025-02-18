"""
Problema 9: Calcular la suma de los dígitos de un número
Enunciado: Escribe un programa en Python que calcule la suma de los dígitos de un número entero positivo ingresado por el usuario.

Requisitos:

1.- El programa debe pedir al usuario un número entero positivo.
2.- Debe calcular la suma de los dígitos del número.
3.- Mostrar el resultado de la suma.
"""

def suma_digitos(entero): # Funcion que suma los digitos del entero ingresado
    entero = str(entero) # Convierte el entero a string
    
    suma = 0
    for x in range(len(entero)): # Itera sobre el entero en string
        suma += int(entero[x]) # Cada iteracion convierte al digito a entero y lo suma al total
    
    return suma # Retorna la suma

#########################   Main    ################################

entero = int(input("Ingrese un numero entero:"))

print(f"La suma de los digitos de {entero} es {suma_digitos(entero)}.")