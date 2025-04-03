"""
Se tiene que cargar los votos obtenidos por tres candidatos a una elección.
En una lista cargar en la primer componente el nombre del candidato y en la 
segunda componente cargar una lista con componentes de tipo tupla con el nombre de la 
provincia y la cantidad de votos obtenidos en dicha provincia.
Se deben cargar los datos por teclado, pero si se cargaran por asignación tendría una estructura similar a esta:

candidatos=[ ("juan",[("cordoba",100),("buenos aires",200)]) , ("ana", [("cordoba",55)]) , ("luis", [("buenos aires",20)]) ]

1) Función para cargar todos los candidatos, sus nombres y las provincias con los votos obtenidos.
2) Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas las provincias.
"""

# Funcion que carga los candidatos, las provincias y la cantidad de votos obtenidos
def cargar():
    candidatos = []
    for x in range(3):
        nom = input("\nIngrese el nombre del candidato: ")
        cantidad = int(input("Ingrese la cantidad de provincias donde recibio votos: "))
        provincias = []
        for y in range(cantidad):
            provin = input("Ingrese el nombre de la provincia: ")
            votos = int(input("Ingrese la cantidad de votos que obtuvo: "))
            provincias.append((provin, votos))
        
        candidatos.append((nom, provincias))
    
    return candidatos

# Funcion que imprime los candidatos y el total de votos que obtuvieron
def imprimir(candidatos):
    print("\nCandidatos y total de votos que obtuvieron:")
    for x in range(len(candidatos)):
        suma = 0
        for y in range(len(candidatos[x][1])):
            suma += candidatos[x][1][y][1]
        print(f"{candidatos[x][0]}: {suma} votos")

#########################   Main    ################################

candidatos = cargar()
print(candidatos)
imprimir(candidatos)