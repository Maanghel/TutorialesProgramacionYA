"""
Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado".
"""
def imprimir_felicitacion(promedio): # Funcion que imprimie felicitado si el promedio es mayor a 7
    if promedio >= 7:
        print("Promocionado.")
    else:
        print("Reprobado.")

nota1 = float(input("Ingrese la primer nota del alumno:"))
nota2 = float(input("Ingrese la segunda nota del alumno:"))
nota3 = float(input("Ingrese la tercer nota del alumno:"))

promedio = (nota1 + nota2 + nota3) / 3

print(f"El promedio es de: {promedio}")
imprimir_felicitacion(promedio)