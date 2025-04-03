"""
Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a mayor. 
En otra función solicitar la carga de 3 enteros por teclado y proceder a llamar a la primer función definida.
"""

# Funcion que ordena de menor a mayor
def ordenar_menor_mayor(lista):
    lista_ordenada = sorted(lista)
    print("\nLista ordenada de menor a mayor:")
    for x in range(3):
        print(lista_ordenada[x])

# Funcion que realiza la carga de 3 enteros
def cargar_enteros():
    lista = []
    for x in range(3):
        valor = int(input("Ingrese un valor: "))
        lista.append(valor)
    
    ordenar_menor_mayor(lista)

#########################   Main    ################################

cargar_enteros()