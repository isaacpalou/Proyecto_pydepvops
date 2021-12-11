def conversion_md(lista_filtrada):
    lista = lista_filtrada
    string = ''
    for diccionario in lista:
        for item in diccionario:
            if item == 'name':
                string += "# **Menu: " + diccionario[item] + '**' + "\n"

            if item == 'plates':
                string += '### Platos: ' + '\n' + '- ' + diccionario[item][0] + '\n' + '- ' + diccionario[item][1] + '\n' + '- ' +  diccionario[item][2] + '\n' + '\n'

            if item == 'drink':
                string += '### Bebida: ' + diccionario[item] + '\n' + '\n'
            
            if item == 'stock':
                string += '### Stock: ' + str(diccionario[item]) + '\n' + '\n'

            if item == 'price':
                string += '### Precio: ' + str(diccionario[item]) + '\n' + '\n'
            
            if item == 'discount':
                string += '### Descuento: ' + str(diccionario[item]) + ' %' + '\n' + '\n' #\n añade espacios, en Markdown se necesitan dos espacios para cambiar de linea.
            
            if item == 'valoration':
                string += '### **Valoracion:** ' + diccionario[item] + '\n' + '<br>' + '\n' + '\n'

    f = open('pagina.md', 'w')
    f.write(string)
    f.close()

if __name__=='__main__':

    d = {   'name': 'Alberto',
            'plates': ["Rollitos de primavera", "Ternera con salsa de ostras", "helado frito"],
            'drink': 'Coca',
            'stock': '8',
            'price': '20000000',
            'discount': '99',
            'valoration': '10.5'
    }

    conversion_md([d])
    