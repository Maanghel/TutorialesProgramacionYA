"""
Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente información: 
cantidad total de preguntas que se le realizaron y la cantidad de preguntas que contestó correctamente. 
Se pide confeccionar un programa que ingrese los dos datos por teclado e informe el nivel del mismo 
según el porcentaje de respuestas correctas que ha obtenido, y sabiendo que:
	Nivel máximo:	Porcentaje>=90%.
	Nivel medio:	Porcentaje>=75% y <90%.
	Nivel regular:	Porcentaje>=50% y <75%.
	Fuera de nivel:	Porcentaje<50%.
"""

def imprimir_nivel(preguntas, correctas): # Funcion que imprime el nivel del estudiante
    resultado = (correctas * 100) // preguntas
    
    if resultado >= 90:
        print("Nivel maximo.")
    elif resultado >= 75 and resultado < 90:
        print("Nivel medio.")
    elif resultado >= 50 and resultado < 75:
        print("Nivel regular.")
    else:
        print("Fuera de nivel.")

#########################   Main    ################################

preguntas = int(input("Ingrese la cantidad de preguntas realizadas: "))
correctas = int(input("Ingrese la cantidad de preguntas contestadas correctamente: "))

imprimir_nivel(preguntas, correctas)