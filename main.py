from pprint import pprint
from src.Acceso_a_datos.conexion_bd import conexion_bd
from src.Acceso_a_datos.extraccion_datos import extraccion_datos
from src.Logica_python.conversion import conversion_md


def main():
    coleccion = conexion_bd()
    lista = extraccion_datos(coleccion)
    # conversion_md(lista)
    return (lista)

if __name__ == '__main__':
    main()
