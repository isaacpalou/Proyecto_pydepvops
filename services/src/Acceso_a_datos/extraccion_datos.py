import pymongo
from pprint import pprint
<<<<<<< HEAD
from conexion_bd import conexion_bd

def extraccion_datos():
    collection = conexion_bd()
=======


def extraccion_datos(coleccion):
    collection = coleccion
>>>>>>> d7e3bc7015324f87821b1359a95e80c0af370d43
    items = collection.find()
    lista = []

    for i in items:
        lista.append(i)
    return lista

<<<<<<< HEAD
if __name__ == '__main__':
    pprint(extraccion_datos())
=======

if __name__ == '__main__':
    extraccion_datos()
>>>>>>> d7e3bc7015324f87821b1359a95e80c0af370d43
