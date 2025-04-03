"""
Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde)
Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas.
Imprimir las dos listas de sueldos.
"""

sueldos_mañana = []
sueldos_tarde = []

for x in range(4):
    sueldo = float(input("Ingrese el sueldo del operador de la mañana: "))
    sueldos_mañana.append(sueldo)

for x in range(4):
    sueldo = float(input("Ingrese el sueldo del operador de la tarde: "))
    sueldos_tarde.append(sueldo)

print(f"\nLista de sueldos de la mañana:\n{sueldos_mañana}")
print(f"\nLista de sueldos de la tarde:\n{sueldos_tarde}")