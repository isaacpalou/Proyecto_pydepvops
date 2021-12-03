import pymongo
from conexion_bd import conexion_bd


# def insercion_datos():
#     collection = conexion_bd()
#     with open("services/src/Acceso a datos/menus.json", "r") as my_json:
#         datos = json.load(my_json)
#     try:
#         collection.insert_many(datos)
#         print("DATOS METIDOS CON ÉXITO")
#     except pymongo.errors.ServerSelectionTimeoutError as error:
#         print("Error al conectar al servidor") % error
#     except pymongo.errors.CollectionInvalid as error:
#         print("No se pudo conectar a MongoCompass") % error


# def borrar_coleccion():
#     collection = conexion_bd()
#     try:
#         collection.drop()
#         print("La coleccion se ha borrado correctamente")
#     except pymongo.errors.ServerSelectionTimeoutError as error:
#         print("Error al conectar al servidor") % error
#     except pymongo.errors.CollectionInvalid as error:
#         print("No se pudo conectar a MongoCompass") % error


# borrar_coleccion()
