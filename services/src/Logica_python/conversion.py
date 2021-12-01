import json

#Converir JSON data a Diccionarios python
data = json.loads({})     #Para decodificar una cadena en el formato JSON (es decir, convertirla a un objeto de Python).
json.dumps()

# Opening JSON file
with open ('data.json') as json_file:
    data = json.load(# json file in data base)
print(data['data.json'])