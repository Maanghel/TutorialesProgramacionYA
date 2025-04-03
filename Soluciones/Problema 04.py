"""
Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas y el valor por hora.
"""

def sueldo_mensual(horas, valor_hora): # Funcion que calcula el sueldo mensual
    return horas * valor_hora # Retorna la multiplicacion de las horas por el valor

#########################   Main    ################################

horas = int(input("Ingrese la cantidad de horas trabajadas: "))
valor_hora = float(input("Ingrese a cuanto se paga la hora: "))

print(f"El sueldo mensual del operador es: {sueldo_mensual(horas, valor_hora)}")