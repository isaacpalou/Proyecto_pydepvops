import pymongo
from pymongo import MongoClient


# Este código lo que hace és devolver la colección "menus"
def conexion_bd():
    # Link del cluster al que te quieres conectar.
    uri = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.qvf0j.mongodb.net/test"
    client = MongoClient(uri)
    # Base de datos que quieres seleccionar.
    db = client.PYDEVOPS
    return db.menus


# if __name__ == '__main__':
#     assert conexion_bd() == True
