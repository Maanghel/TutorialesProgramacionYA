"""
Confeccionar un programa que solicite la carga de 10 valores reales por teclado. 
Mostrar al final su suma. Definir varias líneas de comentarios indicando el nombre del 
programa, el programador y la fecha de la última modificación. Utilizar el caracter # para los comentarios.
"""

# Programa: Carga de 10 Numeros
# Programador: Manuel Gamez
# Fecha de última modificación: 19/10/2024

def sumar_enteros(enteros): # Funcion que suma los enteros de una lista
    return sum(enteros) # Retorna la suma de todos los enteros

#########################   Main    ################################

lista_enteros = []

for x in range(10): # Inicia un bucle de repeticion de 10 vueltas
    entero = int(input("Ingrese un entero: "))
    lista_enteros.append(entero)

print(f"\nLa suma de los enteros ingresados es de: {sumar_enteros(lista_enteros)}")