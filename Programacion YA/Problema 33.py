"""
Realizar un programa que solicite la carga de valores enteros por teclado y los sume. 
Finalizar la carga al ingresar el valor -1. Dejar como comentario dentro del código fuente el enunciado del problema.
"""

def sumar_enteros(enteros): # Funcion que suma los enteros de una lista
    return sum(enteros) # Retorna la suma de todos los enteros

#########################   Main    ################################

lista_enteros = []

centinela = True # Variable que indicara cuando el while finalizara
while centinela:
    entero = int(input("Ingrese un entero (-1 para finalizar): "))
    
    if entero == -1:
        centinela = False
    else:
        lista_enteros.append(entero)

print(f"\nLa suma de los enteros ingresados es de: {sumar_enteros(lista_enteros)}")