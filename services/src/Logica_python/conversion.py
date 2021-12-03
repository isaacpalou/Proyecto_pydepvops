# import sys
# sys.path.append(".")


from pprint import pprint

from ..Acceso_a_datos.extraccion_datos import extraccion_datos

def equisde():
    lista = extraccion_datos()
    pprint(lista)

equisde()