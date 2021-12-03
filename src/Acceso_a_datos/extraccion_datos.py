import pymongo
from pprint import pprint


def extraccion_datos(coleccion):
    collection = coleccion
    items = collection.find()
    lista = []

    for i in items:
        lista.append(i)
    return lista


if __name__ == '__main__':
    extraccion_datos()
