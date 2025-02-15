"""
Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
    a) La cantidad de valores ingresados negativos.
    b) La cantidad de valores ingresados positivos.
    c) La cantidad de múltiplos de 15.
    d) El valor acumulado de los números ingresados que son pares.
"""

def verificar_enteros(cadena): # Funcion que contabiliza los positivos, negativos, multiplos de 15 y suma los pares de una lista de enteros
    lista_enteros = list(map(int, cadena.split()))
    
    negativos = 0
    positivos = 0
    multiplos_15 = 0
    suma_pares = 0
    for entero in lista_enteros:
        if entero < 0:
            negativos += 1
        elif entero > 0:
            positivos += 1
            if entero % 15 == 0:
                multiplos_15 += 1
            if entero % 2 == 0:
                suma_pares += entero
    
    return [positivos, negativos, multiplos_15, suma_pares]

#########################   Main    ################################

enteros = input("Ingrese una lista de enteros (separados por espacios): ")

positivos, negativos, multiplos_15, suma_pares = verificar_enteros(enteros)

print(f"\nPositivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Multiplos de 15: {multiplos_15}")
print(f"Suma de los numeros pares: {suma_pares}")