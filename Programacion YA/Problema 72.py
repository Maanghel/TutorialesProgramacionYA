"""
Definir una lista de enteros por asignación en el bloque principal.
Llamar a una función que reciba la lista y nos retorne el producto de todos sus elementos. 
Mostrar dicho producto en el bloque principal de nuestro programa.
"""

# Funcion que retorna el producto de todos los enteros de una lista
def producto_lista(lista):
    producto = 1
    for x in range(len(lista)):
        producto *= lista[x]
    
    return producto

#########################   Main    ################################

lista_enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Lista: {lista_enteros}")
print(f"\nEl producto de todos los elementos es {producto_lista(lista_enteros)}.")