"""
Crear una lista de enteros por asignación. Definir una función que reciba una lista de enteros
y un segundo parámetro de tipo entero. 
Dentro de la función mostrar cada elemento de la lista multiplicado por el valor entero enviado.
"""

# Funcion que imprime la lista multiplicada por el entero indicado
def imprimir_lista_multiplicada(lista, entero):
    print(f"\nLista multiplicada por {entero}:")
    for x in range(len(lista)):
        print(lista[x] * entero)

#########################   Main    ################################

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nLista original:")
for x in range(len(lista)):
    print(lista[x])
    
imprimir_lista_multiplicada(lista, 10)