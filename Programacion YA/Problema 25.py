"""
Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base y la altura de un triángulo. 
El programa deberá informar:
    a) De cada triángulo la medida de su base, su altura y su superficie.
    b) La cantidad de triángulos cuya superficie es mayor a 12.
"""

def superficie_triangulo(cantidad): # Funcion que saca la superficie de un triangulo y despues lo suma si es mayor a 12
    superficie_mayor = 0
    for x in range(cantidad):
        base = int(input("Ingrese la base del triangulo: "))
        altura = int(input("Ingrese la altura del triangulo: "))
        
        promedio = base * altura
        
        print(f"La base del triangulo es de {base} y su altura es de {altura} por lo tanto su promedio es de {promedio}.")
        
        if promedio > 12:
            superficie_mayor += 1
    
    print(f"El total de triangulos cuya superficie es mayor a 12 son {superficie_mayor}")

#########################   Main    ################################

total = int(input("Ingrese el total de triangulos a verificar: "))
superficie_triangulo(total)