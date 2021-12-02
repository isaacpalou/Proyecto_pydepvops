import sys
sys.path.append(".")

from services.src.Acceso_a_datos.extraccion_datos import extraccion_datos
from pprint import pprint
def equisde():
    lista2 = extraccion_datos()
    pprint(lista2)
equisde()