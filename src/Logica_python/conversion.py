# import sys
# sys.path.append(".")
<<<<<<< HEAD


from pprint import pprint

from ..Acceso_a_datos.extraccion_datos import extraccion_datos

def equisde():
    lista = extraccion_datos()
    pprint(lista)

equisde()
=======

from pprint import pprint

from Acceso_a_datos.extraccion_datos import extraccion_datos


def equisde(lista):
    pprint(lista)
# equisde()
>>>>>>> d7e3bc7015324f87821b1359a95e80c0af370d43
