from pprint import pprint


def conversion_md(listo):
    pero = listo
    string = ''
    for diccionario in pero:
        for i in diccionario:
            if i == 'name':
                string += "# Menu: " + diccionario[i] + "\n"
    with open('pagina.md', 'a', encoding="UTF-8") as f:
        f.write(string)
