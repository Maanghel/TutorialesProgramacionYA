"""
Realizar un programa que contenga las siguientes funciones:
1) Carga de una lista de 10 enteros.
2) Recibir una lista y retornar otra con la primer mitad (se sabe que siempre llega una lista con una cantidad par de elementos)
3) Imprimir una lista.
"""

# Funcion que carga diez enteros en una lista
def carga():
    lista = []
    for x in range(10):
        entero = int(input("Ingrese un entero: "))
        lista.append(entero)
    
    return lista

# Funcion que retorna la mitad de la lista dada por medio de slicing
def mitad_lista(lista):
    return lista[:5]

# funcion que imprime una lista
def imprimir(lista):
    for entero in lista:
        print(entero)

#########################   Main    ################################

lista1 = carga()
lista2 = mitad_lista(lista1)

print(f"\nLista de enteros original:")
imprimir(lista1)
print(f"\nLista con la mitad de la primera lista:")
imprimir(lista2)