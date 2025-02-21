"""
Almacenar en una lista 5 empleados, cada elemento de la lista es una sub 
lista con el nombre del empleado junto a sus últimos tres sueldos (estos tres valores en una tupla)
El programa debe tener las siguientes funciones:
1)Carga de los nombres de empleados y sus últimos tres sueldos.
2)Imprimir el monto total cobrado por cada empleado.
3)Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a 10000 en los últimos tres meses.
Tener en cuenta que la estructura de datos si se carga por asignación debería ser similar a:
empleados = [["juan",(2000,3000,4233)] , ["ana",(3444,1000,5333)] ,  etc.   ]
"""

def carga():
    empleados = []
    for x in range(5):
        nom = input("\nIngrese el nombre del empleado: ")
        sueldo1 = float(input("Ingrese el primer sueldo: "))
        sueldo2 = float(input("Ingrese el segundo sueldo: "))
        sueldo3 = float(input("Ingrese el tercer sueldo: "))
        
        empleados.append([nom, (sueldo1, sueldo2, sueldo3)])
    
    return empleados

def imprimir_total_sueldo(empleados):
    for x in range(len(empleados)):
        print(f"\nEl empleado {empleados[x][0]} gano un total de: {empleados[x][1][0] + empleados[x][1][1] + empleados[x][1][2]}")

def imprimir_mayor10000(empleados):
    print("\nEmpleados con ingresos superiores a $10000:")
    for x in range(len(empleados)):
        total = empleados[x][1][0] + empleados[x][1][1] + empleados[x][1][2]
        if total >= 10000:
            print(empleados[x][0])
            
#########################   Main    ################################

empleados = carga()
imprimir_total_sueldo(empleados)
imprimir_mayor10000(empleados)