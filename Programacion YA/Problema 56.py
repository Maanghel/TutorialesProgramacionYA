"""
Crear una lista por asignación con la cantidad de elementos de tipo lista que usted desee.
Luego imprimir el último elemento de la lista principal.
"""

def imprimir_ultimo_elemento(lista):
    return lista[-1]

#########################   Main    ################################

lista = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

print(f"El ultimo elemento de la lista es: {imprimir_ultimo_elemento(lista)}")