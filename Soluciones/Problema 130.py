from urllib import request
import json

def descargar_datos(url):
    pagina = request.urlopen(url)
    datos = pagina.read().decode("utf-8")
    lista = json.loads(datos)
    return lista

def imprimir_datos(lista):
    for elemento in lista:
        print(f"Id: {elemento["id"]}")
        print(f"name: { elemento["name"]}")
        print(f"username: {elemento["username"]}")
        print(f"email: {elemento["email"]}")
        print(f"street: {elemento["address"]["street"]}")
        print(f"suite: {elemento["address"]["suite"]}")    
        print(f"city: {elemento["address"]["city"]}")
        print(f"zipcode: {elemento["address"]["zipcode"]}")
        print(f"lat: {elemento["address"]["geo"]["lat"]}")
        print(f"lng: {elemento["address"]["geo"]["lng"]}")
        print(f"phone: {elemento['phone']}")
        print(f"website: {elemento["website"]}")
        print(f"company name: {elemento["company"]["name"]}")
        print(f"catchPhrase: {elemento["company"]["catchPhrase"]}")
        print(f"bs: {elemento["company"]["bs"]}")
        print("_" * 80)

#########################   Main    ################################

lista = descargar_datos("https://jsonplaceholder.typicode.com/users")
imprimir_datos(lista)