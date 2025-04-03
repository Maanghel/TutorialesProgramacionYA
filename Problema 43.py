"""
Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas más bajas.
"""

def promedio_alturas(alturas): # Funcion que saca el promedio de las alturas
    return sum(alturas) / len(alturas) # Retorna el promedio

def mas_altas_promedio(alturas): # Funcion que saca el total de personas mas bajas y mas altas que el promedio
    promedio = promedio_alturas(alturas)
    
    total_altas = 0
    total_bajas = 0
    for altura in alturas:
        if altura > promedio:
            total_altas += 1
        else:
            total_bajas += 1
    
    return [total_altas, total_bajas] # Retorna 2 elementos en una lista

#########################   Main    ################################

lista_alturas = []
for x in range(5):
    altura = float(input("Ingrese la altura de la persona: "))
    lista_alturas.append(altura)

print(f"\nLas alturas ingresadas son:\n{lista_alturas}")
print(f"\nEl promedio de las alturas ingresadas es de: {promedio_alturas(lista_alturas)}")

mas_altas, mas_bajas = mas_altas_promedio(lista_alturas)

print(f"\nEl total de las personas que miden mas que el promedio es de: {mas_altas}")
print(f"\nEl total de las personas que miden menos que el promedio es de: {mas_bajas}")