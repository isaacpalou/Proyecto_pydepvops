import pymongo
from pprint import pprint
from conexion_bd import conexion_bd

def extraccion_datos():
    collection = conexion_bd()
    items = collection.find()
    lista = []

    for i in items:
        lista.append(i)
    return lista

if __name__ == '__main__':
    pprint(extraccion_datos())