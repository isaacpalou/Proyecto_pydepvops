from threading import main_thread
from pymongo import MongoClient


def conexion_bd():
    try:
    # Link del cluster al que te quieres conectar.
        uri = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.qvf0j.mongodb.net/test"
        client = MongoClient(uri)
    # Base de datos que quieres seleccionar.
        db = client.PYDEVOPS.find()
        lista = []

        for i in db:
            lista.append(i)
    except errors.OperationFailure:
        print("No se ha podido establecer conexion con la base de datos")
    else:
        print("Conexion con la base de datos establecida correctamente")
    finally:
        return lista

# Casos test añadidos