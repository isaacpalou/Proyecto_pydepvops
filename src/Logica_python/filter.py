def low_filter(lista):
    low_list = lista
    output = []
    for element in low_list:
        if float(element['valoration']) < 4:
            output.append(element)
    return output


def medium_filter(lista):
    medium_list = lista
    output = []
    for element in medium_list:
        if float(element['valoration']) >= 4 and float(element['valoration']) < 4.4:
            output.append(element)
    return output


def high_filter(lista):
    high_list = lista
    output = []
    for element in high_list:
        if float(element['valoration']) >= 4.4:
            output.append(element)
    return output
