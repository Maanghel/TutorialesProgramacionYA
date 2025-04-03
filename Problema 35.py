"""
Realizar la carga de dos nombres de personas distintos. 
Mostrar por pantalla luego ordenados en forma alfabética.
"""

def ordenar_alfabeticamente(nombres): # Ordena alfabeticamente los nombres
    return sorted(nombres) # Retorna los nombres ordenados alfabeticamente

#########################   Main    ################################

lista_nombres = []

for x in range(2):
    nombre = input("Ingrese un nombre: ")
    lista_nombres.append(nombre)

nombres_ordenados = ordenar_alfabeticamente(lista_nombres) # Asigna el resultado a una variable

print(f"Nombres ordenados:\n1.-{nombres_ordenados[0]}\n2.-{nombres_ordenados[1]}") # Imprime los valores de la lista