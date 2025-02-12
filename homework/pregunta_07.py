import csv

def pregunta_07():

    route = "files/input/data.csv"
    # diccionario que almacena los registros
    dict = {}

    with open(route, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')

        for line in lector_csv:
            # Se toma una linea de la columna 5
            num= int(line[1])
            
            # Si no esta en el diccionario, se crea
            if num not in dict:
                dict[num] = [line[0]]
            # Se añaden letras al diccionario en caso de que ya exista su clave
            else:
                dict[num].append(line[0])
        

    # Se ponen en formato de tupla  se ordena en base a su número(menor a mayor)
    lista = [(key, value) for key, value in sorted(dict.items())]
    
    return lista