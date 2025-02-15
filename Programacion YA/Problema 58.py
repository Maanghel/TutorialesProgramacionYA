"""
Definir una lista y almacenar los nombres de 3 empleados.
Por otro lado definir otra lista y almacenar en cada elemento una sublista con los números de días del mes que el empleado faltó.
Imprimir los nombres de empleados y los días que faltó.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el nombre o los nombres de empleados que faltaron menos días.
"""

def cargar_inasistencias():
    empleados = []
    faltas = []
    
    for x in range(3):
        nom = input("Ingrese el nombre del empleado: ")
        dias = []
        cant = int(input("Ingrese la cantidad de dias que falto: "))
        for y in range(cant):
            dias.append(int(input(f"Ingrese el dia que falto: ")))
        
        empleados.append(nom), faltas.append(dias)
    
    return [empleados, faltas]

def imprimir_inasistencias(empleados, faltas):
    for x in range(3):
        print(f"\nNombre del empleado: {empleados[x]}")
        print(f"Dias que falto: {faltas[x]}")

def imprimir_cantidad_inasistencias(empleados, faltas):
    for x in range(3):
        print(f"\nNombre del empleado: {empleados[x]}")
        print(f"Cantidad de inasistencias: {len(faltas[x])}")

def imprimir_empleado_menos_inasistencias(empleados, faltas):
    menor = len(faltas[0])
    empleados_menos = []
    
    for x in range(3):
        if len(faltas[x]) < menor:
            menor = len(faltas[x])
            empleados_menos = [empleados[x]]
        elif len(faltas[x]) == menor:
            empleados_menos.append(empleados[x])
    
    print(f"\nEmpleados con menos inasistencias:")
    for x in range(len(empleados_menos)):
        print(empleados_menos[x])

#########################   Main    ################################

empleados, faltas = cargar_inasistencias()
imprimir_inasistencias(empleados, faltas)
imprimir_cantidad_inasistencias(empleados, faltas)
imprimir_empleado_menos_inasistencias(empleados, faltas)