"""
Cargar una lista con 5 elementos enteros. 
Imprimir el mayor y un mensaje si se repite dentro de la lista 
(es decir si dicho valor se encuentra en 2 o más posiciones en la lista)
"""

def mayor_entero(enteros): # Funcion que devuelve el mayor de la lista
    mayor = enteros[0] # Coloca al mayor en la posicion 0
    
    for x in range(1,len(enteros)):
        if enteros[x] > mayor: # Si el valor del elemento actual es mayor al de la variable mayor devuelve True
            mayor = enteros[x] # Asigna el nuevo valor mayor
    
    # mayor = max(enteros) # Otra manera de conseguir el mayor usando la funcion max, el cual devuelve el mayor de una lista
    
    return mayor

def entero_repetido(enteros):
    mayor = mayor_entero(enteros)
    
    contador = 0
    for entero in enteros:
        if entero == mayor:
            contador += 1
    
    if contador == 1:
        print("El numero no se repite en la lista.")
    else:
        print(f"El numero se repite {contador} veces en la lista.")

#########################   Main    ################################

lista_enteros = []

for x in range(5):
    entero = int(input("Ingrese un entero: "))
    lista_enteros.append(entero)

print(f"El Mayor de los numeros ingresados es: {mayor_entero(lista_enteros)}")

entero_repetido(lista_enteros)