##### FUNCIONES QUE FILTRAN EL ELEMENTO "VALORATION" DE LOS JSON PARA ORDENARLOS EN 3 SECCIONES #####

# Funcion que filtra los items cuya valoracion és menor que 4.
def low_filter(lista):
    low_list = lista
    output = []
    for element in low_list:
        if float(element['valoration']) < 4:
            output.append(element)
    return output

# Funcion que filtra los items cuya valoracion és mayor o igual que 4 y menor que 4.4.

#refactorizar variable de valoracion
def medium_filter(lista):
    medium_list = lista
    output = []
    for element in medium_list:
        if float(element['valoration']) >= 4 and float(element['valoration']) < 4.4:
            output.append(element)
    return output

# Funcion que filtra los items cuya valoracion és mayor o igual que 4.4.


def high_filter(lista):
    high_list = lista
    output = []
    for element in high_list:
        if float(element['valoration']) >= 4.4:
            output.append(element)
    return output
