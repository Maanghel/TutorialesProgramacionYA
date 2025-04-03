"""
Crear y cargar en una lisa los nombres de 5 paises y en otra lista paralela
la cantidad de habitantes del mismo. Ordenar alfabeticamente e imprimir
los resultados. Por ultimo ordenar con respecto a la cantidad de habitantes
(de mayor a menor) e imprimir nuevamente.
"""

# Funcion que ordena alfabeticamente los paises
def ordenar_alfabeticamente(paises, total_habitantes):
    for x in range(4):
        for y in range(4):
            if paises[y] > paises[y+1]: # ordena las listas
                aux1 = paises[y]
                paises[y] = paises[y+1]
                paises[y+1] = aux1
                aux2 = total_habitantes[y]
                total_habitantes[y] = total_habitantes[y+1]
                total_habitantes[y+1] = aux2
    
    return [paises, total_habitantes]

# Funcion que ordena la lista de mayor a menor cantidad de habitantes
def ordenar_mayor_menor(paises, total_habitantes):
    for x in range(4):
        for y in range(4):
            if total_habitantes[y] < total_habitantes[y+1]:
                aux1 = total_habitantes[y]
                total_habitantes[y] = total_habitantes[y+1]
                total_habitantes[y+1] = aux1
                aux2 = paises[y]
                paises[y] = paises[y+1]
                paises[y+1] = aux2
    
    return [paises, total_habitantes]

#########################   Main    ################################

lista_paises = [] 
habitantes = []

for x in range(5):
    nom = input("\nIngresa el nombre del pais: ")
    total = int(input("Ingrese el total de habitantes: "))
    lista_paises.append(nom), habitantes.append(total)

paises, habitantes = ordenar_alfabeticamente(lista_paises, habitantes)
print(f"\nLista ordenada de manera alfabeticamente:")
for x in range(len(paises)):
    print(f"{paises[x]} - {habitantes[x]}")

paises, habitantes = ordenar_mayor_menor(lista_paises, habitantes)
print(f"\nLista ordenada de menor a mayor habitantes:")
for x in range(len(paises)):
    print(f"{paises[x]} - {habitantes[x]}")