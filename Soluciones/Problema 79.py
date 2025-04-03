"""
Confeccionar un programa con las siguientes funciones:
1)Cargar una lista de 5 enteros.
2)Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.
"""

# Funcion que carga cinco enteros
def carga():
    lista = []
    for x in range(5):
        lista.append(int(input("Ingrese un entero: ")))
    
    return lista

# Funcion que retorna en una tupla el mayor y el menor de una lista
def mayor_menor(lista):
    mayor = lista[0]
    menor = lista[0]
    for x in range(1, len(lista)):
        if lista[x] > mayor:
            mayor = lista[x]
        if lista[x] < menor:
            menor = lista[x]
    
    return (mayor, menor)

#########################   Main    ################################

lista = carga()
mayor, menor = mayor_menor(lista)

print(f"El mayor de los numeroes ingresados es: {mayor}")
print(f"El menor de los numeros ingresados es: {menor}")