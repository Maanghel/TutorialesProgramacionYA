"""
Confeccionar una programa con las siguientes funciones:
1) Generar una lista con 4 elementos enteros aleatorios comprendidos entre 1 y 3. Agregar un quinto elemento con un 1.
2) Controlar que el primer elemento de la lista sea un 1, en el caso que haya un 2 o 3 mezclar la lista y volver a controlar hasta que haya un 1.
3) Imprimir la lista.
"""

import random

# Funcion que genera una lista de 4 enteros comprendidos entre el 1 y el 3
def generar():
    lista = []
    for x in range(4):
        lista.append(random.randint(1,3))
    lista.append(1)
    
    return lista

# Funcion que mezcla la lista hasta tener un 1 en el inicio de la lista
def controlar_primero(lista):
    while lista[0] != 1:
        random.shuffle(lista)
    
    return lista

# Imprime una lista
def imprimir(lista):
    for entero in lista:
        print(entero)

#########################   Main    ################################

lista = generar()
print("\nLista original:")
imprimir(lista)

controlar_primero(lista)
print("\nLista mezclada:")
imprimir(lista)
