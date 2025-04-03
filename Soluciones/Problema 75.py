"""
Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos.
3) Imprimir las dos listas generadas.
"""

# Funcion que carga una lista de enteros
def carga():
    lista = []
    for x in range(10):
        valor = int(input("Ingrese un entero: "))
        lista.append(valor)
    
    return lista

# Funcion que genera dos listas, una de positivos y una de negativos
def dividir_negativos_positivos(lista):
    lista_positivos = []
    lista_negativos = []
    
    for valor in lista:
        if valor >= 0:
            lista_positivos.append(valor)
        else:
            lista_negativos.append(valor)
    
    return [lista_positivos, lista_negativos]

# Funcion que imprime una lista
def imprimir_lista(lista):
    for valor in lista:
        print(valor)

#########################   Main    ################################

lista_enteros = carga()
lista_positivos, lista_negativos = dividir_negativos_positivos(lista_enteros)
print("\nLista de valores positivos:")
imprimir_lista(lista_positivos)
print("\nLista de valores negativos:")
imprimir_lista(lista_negativos)