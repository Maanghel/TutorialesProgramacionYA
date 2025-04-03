"""
Almacenar en una lista los sueldos (valores float) de 5 operarios. 
Imprimir la lista y el promedio de sueldos.
"""

def promedio_sueldos(sueldos): # Funcion que saca el promedio de sueldos de una lista
    return sum(sueldos) / len(sueldos)

#########################   Main    ################################

lista_sueldos = []
for x in range(5):
    sueldo = float(input("Ingrese el sueldo del operario: "))
    lista_sueldos.append(sueldo)

print(f"\nLista de sueldos:\n{lista_sueldos}")
print(f"\nEl promedio de los sueldos ingresados es de: {promedio_sueldos(lista_sueldos)}")