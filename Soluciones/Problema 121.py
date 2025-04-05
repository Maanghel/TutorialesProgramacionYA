"""
Crear una aplicacion que haga uso de manejo de excepciones
en Python
"""

def cuadrado_perimetro():
    while True:
        try:
            lado = int(input("Ingrese la longitud de uno de los lados: "))
            print(f"El perimetro del cuadrado es de {lado * 4}")
        except ValueError:
            print("Debe ingresar solo valores numericos.")
        
        respuesta = input("\nDesea Ingresar otro valor?[s/n]")
        if respuesta == "n":
            break

#########################   Main    ################################

cuadrado_perimetro()