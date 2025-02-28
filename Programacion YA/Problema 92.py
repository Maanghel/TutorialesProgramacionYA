"""
Confeccionar un programa que genere un número aleatorio entre 1 y 100 y no se muestre.
El operador debe tratar de adivinar el número ingresado.
Cada vez que ingrese un número mostrar un mensaje "Gano" si es igual al generado o "El número aleatorio es mayor" o "El número aleatorio es menor".
Mostrar cuando gana el jugador cuantos intentos necesitó.
"""

import random

# Funcion que genera un numero aleatorio
def generar_numero_aleatorio():
    return random.randint(1, 100)

# Funcion que permite al usuario adivinar el numero y contabiliza sus intentos
def adivinar(numero_aleatorio):
    intentos = 0
    while True:
        numero = int(input("¿Cual es el numero que se genero aleatoriamente? "))
        intentos += 1
        
        if numero == numero_aleatorio:
            print("\nGano.")
            break
        elif numero > numero_aleatorio:
            print("\nEl numero aleatorio es menor.")
        else:
            print("\nEl numero aleatorio es mayor.")
    
    return intentos

#########################   Main    ################################

numero_aleatorio = generar_numero_aleatorio()
intentos = adivinar(numero_aleatorio)
print(f"\nEl operador gano en {intentos} intentos.")