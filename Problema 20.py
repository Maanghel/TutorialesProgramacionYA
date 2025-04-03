"""
En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un 
programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran 
entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar el 
importe que gasta la empresa en sueldos al personal.
"""

def sueldos(total_empleados): # Funcion que verifica el total de importe de una empresa
    suma_sueldos = 0
    sueldos_entre100300 = 0
    for x in range(total_empleados):
        sueldo = float(input("Ingrese el sueldo del empleado: "))
        suma_sueldos += sueldo
        
        if sueldo >= 100 and sueldo <= 300:
            sueldos_entre100300 += 1
    
    return [suma_sueldos, sueldos_entre100300]

#########################   Main    ################################

total_empleados = int(input("Ingrese el total de empleados a verificar: "))

total_importe, sueldos_entre = sueldos(total_empleados)

print(f"El total de empleados que tienen un sueldo entre $100 y $300 es de: {sueldos_entre}.")
print(f"El total de importe que gasta la empresa es de: {total_importe}.")