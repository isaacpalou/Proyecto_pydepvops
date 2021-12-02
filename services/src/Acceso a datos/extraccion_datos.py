import pymongo
from pprint import pprint
from conexion_bd import conexion_bd
def extraccion_datos():
    collection = conexion_bd()
    items = collection.find()
    lista = []

    for i in items:
        lista.append(i)
    pprint(lista)

extraccion_datos()