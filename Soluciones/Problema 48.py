"""
En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente:
a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, 
    colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.
"""

def generar_lista_alumnos(): # Funcion que genera dos listas que son paralelas
    lista_alumnos = []
    lista_calificaciones = []
    
    for x in range(4):
        nombre = input("Ingrese el nombre del alumno: ")
        lista_alumnos.append(nombre)
        calificacion = float(input("Ingrese la calificacion del alumno (1-10): "))
        lista_calificaciones.append(calificacion)
    
    return [lista_alumnos, lista_calificaciones]

def imprimir_listado_condicion(lista_alumnos, lista_calificaciones): # Funcion que imprime un listado con las listas y la condicion de los alumnos
    contador_muybuenos = 0
    for x in range(len(lista_alumnos)):
        if lista_calificaciones[x] >= 8:
            print(f"\nAlumno: {lista_alumnos[x]}\tCalificacion: {lista_calificaciones[x]}\tCondicion: Muy bueno")
            contador_muybuenos += 1
        elif lista_calificaciones[x] < 8 and lista_calificaciones[x] >= 4:
            print(f"\nAlumno: {lista_alumnos[x]}\tCalificacion: {lista_calificaciones[x]}\tCondicion: Bueno")
        else:
            print(f"\nAlumno: {lista_alumnos[x]}\tCalificacion: {lista_calificaciones[x]}\tCondicion: Regular")
    
    print(f'\nEl total de alumnos en la condicion de "Muy bueno" es de: {contador_muybuenos}')

#########################   Main    ################################

lista_alumnos, lista_calificaciones = generar_lista_alumnos()

imprimir_listado_condicion(lista_alumnos, lista_calificaciones)