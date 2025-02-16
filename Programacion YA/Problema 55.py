"""
Se tiene la siguiente lista:
lista=[[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]
Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 10 contenidos en todos los elementos de la variable "lista".
Volver a imprimir la lista.
"""

# Funcion que fija el valor en 0 de los elementos mayores a 10 contenidos en la lista
def fijar_valor(lista):
    for x in range(len(lista)):
        for y in range(len(lista[x])):
            if lista[x][y] > 10:
                lista[x][y] = 0
    
    return lista

#########################   Main    ################################

lista = [[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]

print(f"Lista original:")
for x in range(len(lista)):
    print(lista[x])

lista = fijar_valor(lista)

print(f"\nLista con valores mayores a 10 fijados a 0:")
for x in range(len(lista)):
    print(lista[x])
