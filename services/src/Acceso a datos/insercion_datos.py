from pymongo import MongoClient
import json
from conexion_bd import conexion_bd


def insercion_datos():
    collection = conexion_bd()
    with open("services/src/Acceso a datos/menus.json", "r") as my_json:
        datos = json.load(my_json)
    collection.insert_many(datos)
    print("prueba")
    print("prueba 2")
