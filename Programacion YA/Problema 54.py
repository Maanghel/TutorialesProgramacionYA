"""
Se tiene la siguiente lista:
lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 50 del primer elemento de "lista".
Volver a imprimir la lista.
"""

# Funcion que fija el valor en 0 de los elementos mayores a 50 contenidos en el primer componente de la lista
def fijar_valor(lista):
    for x in range(len(lista[0])): # El for se repetira segun tantos componentes tenga el componente 0 de la lista
        if lista[0][x] > 50:
            lista[0][x] = 0
    
    return lista

#########################   Main    ################################

lista = [[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]

print(f"Lista original:")
for x in range(len(lista)):
    print(lista[x])

lista = fijar_valor(lista)

print(f"\nLista con valores mayores a 50 fijados a 0:")
for x in range(len(lista)):
    print(lista[x])