"""
Definir una lista por asignación con 5 enteros. 
Mostrar por pantalla solo los elementos con valor iguales o superiores a 7.
"""

def mayores_7(enteros): # Funcion que genera una lista con los valores iguales o superiores a 7
    lista_mayores = []
    
    for entero in enteros:
        if entero >= 7:
            lista_mayores.append(entero)
    
    return lista_mayores

#########################   Main    ################################

lista_enteros = [1, 7, 2, 8, 2]

print(f"Lista de enteros:\n{lista_enteros}")
print(f"Los enteros mayores o iguales a 7 son:\n{mayores_7(lista_enteros)}")