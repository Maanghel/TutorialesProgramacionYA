"""
El sitio web
https://jsonplaceholder.typicode.com/
se puede utilizar para recuperar datos con diferentes formatos (JSON por ejemplo) y probar nuestros algoritmos.

Confeccionar una aplicación en Python que recupere el archivo JSON de la siguiente dirección web:
https://jsonplaceholder.typicode.com/posts
Nos retorna un archivo JSON con un formato similar a:
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit
             molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores 
             neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui 
             aperiam non debitis possimus qui neque nisi nulla"
  }]
Convertir los datos recuperados a una lista y mediante un for mostrar los atributos "userID", "id", "title" y "body".
"""

from urllib import request
import json

def descargar_datos(url):
    pagina = request.urlopen(url)
    datos = pagina.read().decode("utf-8")
    lista = json.loads(datos)
    return lista

def imprimir_datos(lista):
    for elemento in lista:
        print(f"userId: {elemento["userId"]}")
        print(f"Id: {elemento["id"]}")
        print(f"title: {elemento["title"]}")
        print(f"body: {elemento["body"]}")
        print("_" * 80)

#########################   Main    ################################

lista = descargar_datos("https://jsonplaceholder.typicode.com/posts")
imprimir_datos(lista)