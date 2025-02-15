"""
Realizar un programa que permita cargar dos listas de 15 valores cada una. 
Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor 
(mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.
"""

def imprimir_mayor(cadena1, cadena2): # Funcion que imprime cual lista es mayor
    lista_enteros1 = list(map(int, cadena1.split()))
    lista_enteros2 = list(map(int, cadena2.split()))
    
    if sum(lista_enteros1) > sum(lista_enteros2):
        print("Lista 1 mayor.")
    elif sum(lista_enteros2) > sum(lista_enteros1):
        print("Lista 2 mayor.")
    else:
        print("Listas iguales.")

#########################   Main    ################################

cadena1 = input("Ingrese una lista de 15 enteros (separados por espacios): ")
cadena2 = input("Ingrese una segunda lista de 15 enteros (separados por espacios): ")

imprimir_mayor(cadena1, cadena2)