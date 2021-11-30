from pymongo import MongoClient
from pprint import pprint

import pymongo


def conexion_bd():
    try:
        # Link del cluster al que te quieres conectar.
        uri = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.qvf0j.mongodb.net/myFirstDatabase?retryWrites=truew=majority"
        client = MongoClient(uri)
        # Base de datos que quieres seleccionar.
        db = client.PYDEVOPS
        # Coleccion en específico.
        collection = db.menus
    except pymongo.errors.ServerSelectionTimeoutError as error:
        print("Error al conectar") % error
