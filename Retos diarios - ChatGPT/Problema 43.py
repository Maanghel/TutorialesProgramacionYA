"""
Problema 43: Determinar si un número es una potencia de 2
Escribe una función en Python que reciba un número entero positivo y determine si es una potencia de 2. Un número es una potencia de 2 si puede expresarse como 
        2**n
n es un entero no negativo.
"""

def determinar_potencia(numero): # Funcion que determina si un numero es potencia de 2
    if numero < 1:
        return False  # Potencias de 2 son positivas
    
    # Dividimos sucesivamente por 2 hasta que el número ya no sea divisible por 2
    while numero % 2 == 0:
        numero /= 2
    
    return numero == 1  # Si llegamos a 1, es potencia de 2

#########################   Main    ################################

numero = int(input("Ingrese un número: "))

if determinar_potencia(numero):
    print(f"El número {numero} es una potencia de 2.")
else:
    print(f"El número {numero} no es una potencia de 2.")