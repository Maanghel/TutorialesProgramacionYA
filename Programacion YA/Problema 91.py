"""
Confeccionar un programa con las siguientes funciones:
1) Cargar una lista con 5 palabras.
2) Intercambiar la primer palabra con la última.
3) Imprimir la lista
"""

# Funcion que carga una lista de cinco palabras
def cargar():
    lista = []
    for x in range(5):
        palabra = input("Ingrese una palabra: ")
        lista.append(palabra)
    
    return lista

# Funcion que intercambia la primer palabra con la ultima
def intercambiar_primeroultimo(lista):
    aux = lista[0]
    lista[0] = lista[-1]
    lista[-1] = aux
    
    return lista

# Funcion que imprime una lista
def imprimir(lista):
    for palabra in lista:
        print(palabra)

#########################   Main    ################################

lista = cargar()
print("\nLista original:")
imprimir(lista)

intercambiar_primeroultimo(lista)
print("\nLista nueva con el primero y ultima palabra intercambiada:")
imprimir(lista)