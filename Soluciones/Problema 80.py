"""
Confeccionar un programa con las siguientes funciones:
1)Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos valores
2)Una función que reciba como parámetro dos tuplas con los nombres y sueldos de 
empleados y muestre el nombre del empleado con sueldo mayor.
En el bloque principal del programa llamar dos veces a la función de carga y seguidamente 
llamar a la función que muestra el nombre de empleado con sueldo mayor.
# bloque principal

empleado1=cargar_empleado()
empleado2=cargar_empleado()
mayor_sueldo(empleado1,empleado2)
"""

# Funcion que carga un empleado y su sueldo y lo retorna como tupla
def carga():
    empleado = input("\nIngrese el nombre del empleado: ")
    sueldo = float(input("Ingrese el sueldo del empleado: "))
    
    return (empleado, sueldo)

# Funcion que recibe dos tuplas e imprime cual tiene mayor sueldo
def sueldo_mayor(empleado1, empleado2):
    if empleado1[1] > empleado2[1]:
        print(f"\nEl empleado {empleado1[0]} tiene mayor sueldo.")
    else:
        print(f"\nEl empleado {empleado2[0]} tiene mayor sueldo.")


#########################   Main    ################################

empleado1 = carga()
empleado2 = carga()

sueldo_mayor(empleado1, empleado2)