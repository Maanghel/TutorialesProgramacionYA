"""
Crear dos listas paralelas. En la primera ingresar los nombres de empleados y en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como su nombre)
"""

# Funcion que carga el total de empleados en la empresa
def cargar_total_empleados():
    total_empleados = int(input("Ingrese el total de empleados que laboran en la empresa: "))
    
    return total_empleados

# Funcion que carga los nombres y los sueldos de los empleados
def cargar_empleados_sueldos(total_empleados):
    nombres = []
    sueldos = []
    
    for x in range(total_empleados):
        nom = input("Ingrese el nombre del empleado: ")
        suel = float(input("Ingrese el sueldo del empleado: "))
        nombres.append(nom), sueldos.append(suel)
    
    return [nombres, sueldos]

# funcion que borra los sueldos y los respectivos empleados mayores a 10000
def borrar_mayor_10000(total_empleados, nombres, sueldos):
    posicion = 0
    while posicion < len(sueldos):
        if sueldos[posicion] > 10000: # Si el sueldo es mayor a 10000 borra el sueldo y el nombre del empleado
            nombres.pop(posicion)
            sueldos.pop(posicion)
        else:
            posicion += 1

    return [nombres, sueldos]

# Funcion que imprime las listas
def imprimir_listas(nombres, sueldos):
    for x in range(len(nombres)):
        print(f"{nombres[x]} - {sueldos[x]}")

#########################   Main    ################################

total_empleados = cargar_total_empleados()

nombres, sueldos = cargar_empleados_sueldos(total_empleados)
print("\nLista de empleados y sueldos:")
imprimir_listas(nombres, sueldos)

nuevo_nombres, nuevo_sueldos = borrar_mayor_10000(total_empleados, nombres, sueldos)
print("\nNueva lista de empleados y sueldos:")
imprimir_listas(nuevo_nombres, nuevo_sueldos)