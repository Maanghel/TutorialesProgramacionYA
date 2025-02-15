"""
Definir una lista que almacene por asignación los nombres de 5 personas. 
Contar cuantos de esos nombres tienen 5 o más caracteres.
"""

def nombres_mayores5(nombres): # Funcion que genera una lista con los nombres con 5 o mas caracteres
    total_mayores = 0
    
    for nombre in nombres:
        if len(nombre) >= 5:
            total_mayores += 1
    
    return total_mayores

#########################   Main    ################################

lista_nombres = ["Manuel", "Ana", "Angel", "Jose", "Alan"]

print(f"Lista de nombres:\n{lista_nombres}")
print(f"Nombres con 5 o mas caracteres:\n{nombres_mayores5(lista_nombres)}")