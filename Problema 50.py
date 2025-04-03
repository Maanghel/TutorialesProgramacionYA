"""
Crear una lista y almacenar los nombres de 5 paises. Ordenar alfabeticamente la lista e imprimirla.
"""

def ordenar(paises): # Funcion que ordena una lista de paises alfabeticamente
    for x in range(4): # Itera sobre la lista paises
        for y in range(4):
            if paises[y] > paises[y+1]: 
                aux = paises[y]
                paises[y] = paises[y+1]
                paises[y+1] = aux
    
    return paises # Retorna la lista ordenada
    # return sorted(paises) Haciendo uso de la funcion sorted() podemos ordenar la lista de manera alfabetica
    
#########################   Main    ################################

paises = []

for x in range(5):
    pais = input("Ingrese el nombre de un pais para almacenarlo: ")
    paises.append(pais)

paises_ordenados = ordenar(paises) # Asigna en la variable paises_ordenados el resultado de la funcion ordenar

print("\nLista de paises ingresados ordenados.")
for x in range(5):
    print(f"-{paises_ordenados[x]}")