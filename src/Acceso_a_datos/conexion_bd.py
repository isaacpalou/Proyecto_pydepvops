
from pymongo import MongoClient
import certifi
import pymongo
from pprint import pprint


# Este código lo que hace és devolver la colección de la base de datos.
def conexion_bd():
    try:
        # URI és el link del cluster al que te quieres conectar.
        uri = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.qvf0j.mongodb.net/test"
        client = MongoClient(uri, tlsCAFile=certifi.where())
        client.server_info()
        db = client.PYDEVOPS
        return db.menus

    except pymongo.errors.ServerSelectionTimeoutError as error:
        print("Error al conectar al servidor") % error
    except pymongo.errors.CollectionInvalid as error:
        print("No se pudo conectar a MongoCompass") % error


if __name__ == '__main__':
    conexion_bd()
