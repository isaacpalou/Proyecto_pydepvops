from pprint import pprint
from services.src.Acceso_a_datos.conexion_bd import conexion_bd
from services.src.Acceso_a_datos.extraccion_datos import extraccion_datos
from services.src.Logica_python.conversion import equisde


def hola():
    coleccion = conexion_bd()
    lista = extraccion_datos(coleccion)
    equisde(lista)


if __name__ == '__main__':
    hola()
