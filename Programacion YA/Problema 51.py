"""
Solicitar por teclado la cantidad de empleados que tiene la empresa. Crear y cargar una lista con todos los sueldos
de dichos empleados. Imprimir la lista de sueldos ordenados de menor a mayor.
"""

def ordenar_menor_mayor(sueldos, cantidad): # Funcion que ordena de menor a mayor los sueldos
    for x in range(cantidad - 1):
        for y in range(cantidad - x - 1):
            if sueldos[y] > sueldos [y+1]:
                aux = sueldos[y]
                sueldos[y] = sueldos[y+1]
                sueldos[y+1] = aux
    
    return sueldos # Retorna la lista ordenada
    # return sorted(sueldos) Haciendo uso de la funcion sorted() podemos ordenar la lista de menor a mayor

#########################   Main    ################################

sueldos = []

cant_empleados = int(input("Ingrese la cantidad de empleados de la empresa: "))

for x in range(cant_empleados):
    sueldo = float(input("Ingrese el sueldo para almacenarlo: "))
    sueldos.append(sueldo)

print(ordenar_menor_mayor(sueldos, cant_empleados))