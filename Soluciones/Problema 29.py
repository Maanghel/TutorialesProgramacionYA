"""
Realizar un programa que lea los lados de n triángulos, e informar:
    a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
    b) Cantidad de triángulos de cada tipo.
"""

def verificar_tipo_triangulo(lado1, lado2, lado3): # Funcion que verifica el tipo de triangulo segun las medidas de sus lados.
    if lado1 == lado2 and lado1 == lado2:
        return True
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        return False
    else:
        return 

#########################   Main    ################################

cantidad = int(input("Ingrese la cantidad de triangualos a verificar: "))

equilatero = 0; isosceles = 0; escaleno = 0
for x in range(cantidad):
    lado1 = int(input("\nIngrese el valor del primer lado: "))
    lado2 = int(input("Ingrese el valor del segundo lado: "))
    lado3 = int(input("Ingrese el valor del tercer lado: "))
    
    if verificar_tipo_triangulo(lado1, lado2, lado3) == True:
        equilatero += 1
    elif verificar_tipo_triangulo(lado1, lado2, lado3) == False:
        isosceles += 1
    elif verificar_tipo_triangulo(lado1, lado2, lado3) == None:
        escaleno += 1

print(f"\nEquilatero: {equilatero}\nIsosceles: {isosceles}\nEscaleno: {escaleno}")