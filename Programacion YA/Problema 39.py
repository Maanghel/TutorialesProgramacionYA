"""
Definir por asignación una lista con 8 elementos enteros. 
Contar cuantos de dichos valores almacenan un valor superior a 100.
"""

def mayores_100(enteros): # Funcion que cuenta cuantos enteros son mayores a 100
    total_mayores = 0
    
    for entero in enteros:
        if entero > 100:
            total_mayores += 1
    
    return total_mayores

#########################   Main    ################################

lista_enteros = [125, 2, 248, 43, 543, 24, 643, 2]

print(f"La lista es:\n{lista_enteros}")
print(f"El total de enteros que son mayores a 100 son: {mayores_100(lista_enteros)}")