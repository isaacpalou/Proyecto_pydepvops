from pprint import pprint
from src.Acceso_a_datos.conexion_bd import conexion_bd
from src.Acceso_a_datos.extraccion_datos import extraccion_datos
from src.Logica_python.conversion import conversion_md
from src.Logica_python.filter import high_filter, low_filter, medium_filter


def main():
    # CONEXIÓN CON LA BBDD
    coleccion = conexion_bd()
    lista = extraccion_datos(coleccion)
    # FILTRO POR VALORACIÓN
    bajo = low_filter(lista)
    medio = medium_filter(lista)
    alto = high_filter(lista)
    # pprint(bajo)

    # CONVERSION A MD
    conversion_md(bajo, "bajo")
    conversion_md(medio, "medio")
    conversion_md(alto, "alto")


if __name__ == '__main__':
    main()
