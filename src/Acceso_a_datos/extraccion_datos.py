import pymongo

# Funcion que devuelve una lista de diccionarios hecha a partir de la coleccion de la Base de datos.
def extraccion_datos(coleccion):
    collection = coleccion
    items = collection.find()
    lista = []

    for item in items:
        lista.append(item)
    return lista

if __name__ == '__main__':
    extraccion_datos()