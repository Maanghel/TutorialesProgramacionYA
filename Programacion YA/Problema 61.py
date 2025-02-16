"""
Crear una lista de 5 enteros y cargarlos por teclado.
Borrar los elementos mayores o iguales a 10 y generar una nueva lista con dichos valores.
"""

# Funcion que carga los enteros en una lista vacia
def cargar_enteros():
    enteros = []
    for x in range(5):
        entero = int(input("Ingrese un entero: "))
        enteros.append(entero)
    
    return enteros

# Funcion que borra y asigna a una nueva lista los numeros mayores o iguales a 10
def borrar_mayoresiguales_10(enteros):
    nueva_lista = []
    posicion = 0
    
    while posicion < len(enteros):
        if enteros[posicion] >= 10:
            nueva_lista.append(enteros.pop(posicion)) # Agrega los componentes eliminados a la nueva lista
        else:
            posicion += 1
    
    return nueva_lista

# Funcion que imprime una lista
def imprimir_lista(enteros):
    for x in range(len(enteros)):
        print(enteros[x])

#########################   Main    ################################

lista_enteros = cargar_enteros()
print("\nLista de enteros:")
imprimir_lista(lista_enteros)

nueva_lista_enteros = borrar_mayoresiguales_10(lista_enteros)
print("\nLista de enteros eliminador por ser mayores a 10:")
imprimir_lista(nueva_lista_enteros)