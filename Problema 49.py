"""
Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos cada una. 
Generar una tercer lista que surja de la suma de los elementos de la misma posición de cada lista. Mostrar esta tercer lista.
"""

def generar_lista_numericas(): # Funcion que genera dos listas numeros
    lista1 = []
    lista2 = []
    
    for x in range(4):
        numero = int(input("Ingrese un entero para la primer lista: "))
        lista1.append(numero)
    for x in range(4):
        numero = int(input("Ingrese un entero para la segunda lista: "))
        lista2.append(numero)
    
    return [lista1, lista2] # Retorna ambas listas

def generar_lista_suma(lista1, lista2): # Funcion que genera una tercer lista de la suma de cada elemento de las listas
    lista3 = []
    
    for x in range(len(lista1)):
        lista3.append(lista1[x] + lista2[x]) # Agrega a la lista3 la suma del componente de la lista1 y de la lista2
    
    return lista3

#########################   Main    ################################

lista1, lista2 = generar_lista_numericas()

lista3 = generar_lista_suma(lista1, lista2)

print(f"Lista 1: {lista1}\nLista 2: {lista2}")
print(f"La suma de cada elemento en la misma posicion de las dos listas es de: {lista3}")