"""
Desarrollar un programa que cree una lista de 50 elementos. El primer elemento es una lista con un elemento entero, 
el segundo elemento es una lista de dos elementos etc.
La lista debería tener esta estructura y asignarle esos valores a medida que se crean los elementos:
[[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5], etc....]
"""

def crear_lista():
    lista = []
    for x in range(1, 51):
        lista.append(list(range(1, x+1)))
    return lista

#########################   Main    ################################

lista = crear_lista()

print(f"Lista creada:\n {lista}")