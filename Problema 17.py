"""
De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar un programa que lea los datos de entrada e informe:
    a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
    b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %.
    c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios.
"""

def otorgar_aumento(sueldo, antiguedad): # Funcion que imprime el nuevo sueldo segun sea el caso
    if sueldo < 500 and antiguedad >= 10:
        nuevo_sueldo = (sueldo * 0.20) + sueldo
        print(f"Se le otorga un aumento del 20% de su sueldo, su sueldo quedaria en:\n{nuevo_sueldo}")
    elif sueldo < 500 and antiguedad < 10:
        nuevo_sueldo = (sueldo * 0.05) + sueldo
        print(f"Se le otorga un aumento del 5% de su sueldo, su sueldo quedaria en:\n{nuevo_sueldo}")
    elif sueldo >= 500:
        print(f"El sueldo permanece sin cambios: {sueldo}")

#########################   Main    ################################

sueldo = float(input("Ingrese el sueldo del operador: "))
antiguedad = int(input("Ingrese los años de antiguedad: "))

otorgar_aumento(sueldo, antiguedad)