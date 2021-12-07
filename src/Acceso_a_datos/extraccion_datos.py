import pymongo
from pprint import pprint
# Funcion que devuelve una lista de diccionarios hecha a partir de la coleccion de la Base de datos


def extraccion_datos(coleccion):
    # assert isinstance(coleccion, dict)
    collection = coleccion
    items = collection.find()
    lista = []

    for item in items:
        lista.append(item)
    return lista
