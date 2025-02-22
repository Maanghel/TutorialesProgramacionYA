"""
Crear un diccionario en Python para almacenar los datos de empleados de una empresa. 
La clave será su número de legajo y en su valor almacenar una lista con el nombre, profesión y sueldo.
Desarrollar las siguientes funciones:
1) Carga de datos de empleados.
2) Permitir modificar el sueldo de un empleado. Ingresamos su número de legajo para buscarlo.
3) Mostrar todos los datos de empleados que tienen una profesión de "analista de sistemas"
"""

# Funcion que carga un diccionario
def carga():
    empleados = {}
    continuar = "s"
    while continuar == "s":
        numero = int(input("\nIngrese el numero de legajo del empleado: "))
        nombre = input("Ingrese el nombre del empleado: ")
        prof = input("Ingrese la profesion del empleado: ")
        sueldo = float(input("Ingrese el sueldo del empleado: "))
        empleados[numero] = [nombre, prof, sueldo]
        continuar = input("Desea ingresar los datos de otro empleado: [s/n]")
    
    return empleados

# Funcion que imprime el diccionario
def imprimir(empleados):
    print("\nEmpleados:")
    for legajo in empleados:
        print(f"\nNumero de legajo: {legajo}:")
        print(f"Nombre: {empleados[legajo][0]}\nProfesion: {empleados[legajo][1]}\nSueldo: {empleados[legajo][2]}")

# Funcion que modifica el sueldo de un empleado
def modificar_sueldo(empleados):
    seleccion = int(input("\nIngrese el numero de legajo del empleado al que le modificara el sueldo: "))
    if seleccion in empleados:
        empleados[seleccion][2] = float(input(f"Ingrese el nuevo sueldo de {empleados[seleccion][0]}: "))
    else:
        print("No se encuentra un empleado con ese numero de legajo.")

# Funcion que retorna a los empleados con la profesion de analista de sistemas
def consultar(empleados):
    print("\nListado de empleados con profesion de \"Analista de sistemas\":")
    for legajo in empleados:
        if empleados[legajo][1] == "Analista de sistemas":
            print(f"\nNombre: {empleados[legajo][0]}\nProfesion: {empleados[legajo][1]}\nSueldo: {empleados[legajo][2]}")

#########################   Main    ################################

empleados = carga()
imprimir(empleados)
modificar_sueldo(empleados)
imprimir(empleados)
consultar(empleados)