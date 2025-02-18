"""
Problema 22: Encontrar los números duplicados en una lista
Dada una lista de números enteros, debes encontrar todos los números que aparecen 
más de una vez y devolverlos en una lista. Si no hay duplicados, devolver una lista vacía.
"""

def encontrar_duplicados(cadena): # Funcion que encuentra los duplicados de una lista
    lista_enteros = list(map(int, cadena.split())) # Convierte en una lista de enteros la cadena ingresada
    duplicados = set() # Se crea un conjunto de duplicados vacio
    vistos = set() # Se crea un conjunto de vistos vacio

    for numero in lista_enteros: # Itera sobre la lista de enteros
        if numero in vistos: # Si el entero actual esta en vistos, agrega al numero a duplicados
            duplicados.add(numero)
        else:
            vistos.add(numero)
    
    return list(duplicados) # Retorna los duplicados convertidos en lista (como era conjunto los duplicados se eliminaron)

#########################   Main    ################################

cadena = input("Ingrese una lista de números enteros (separados por espacios): ")
duplicados = encontrar_duplicados(cadena)

if duplicados:
    print(f"Los números duplicados son: {duplicados}")
else:
    print("No hay números duplicados.")