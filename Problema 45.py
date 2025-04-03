"""
Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. 
Mostrar el nombre de persona menor en orden alfabético.
"""

def menor_alfabetico(nombres): # Funcion que devuelve el orden con menor 
    menor = nombres[0] # Coloca al menor en la posicion 0
    
    for x in range(1,len(nombres)):
        if nombres[x] < menor: # Si el valor del elemento actual es menor al de la variable menor devuelve True
            menor = nombres[x] # Asigna el nuevo valor menor
    
    # menor = min(nombres) # Otra manera de conseguir el menor usando la funcion min, el cual devuelve el menor de una lista
    
    return menor

#########################   Main    ################################

lista_nombres = []

for x in range(5):
    nombre = input("Introduzca el nombre de la persona: ")
    lista_nombres.append(nombre)

print(f"El menor de los nombres ingresados en orden alfabetico es: {menor_alfabetico(lista_nombres)}")