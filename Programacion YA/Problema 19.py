"""
Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.
"""

def altura_promedio(total_personas): # Verifica la altura promedio de las personas
    suma_alturas = 0
    for x in range(total_personas):
        altura = float(input("Ingrese la altura de la persona: "))
        suma_alturas += altura
    
    promedio = suma_alturas / total_personas
    
    return promedio

#########################   Main    ################################

total_personas = int(input("Ingrese el total de personas a verificar: "))

print(f"El promedio de altura de las personas ingresadas es de: {altura_promedio(total_personas)}")