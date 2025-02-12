
import csv


def pregunta_12():

    route = "files/input/data.csv"
    # diccionario que almacena los registros
    dict = {}

    with open(route, 'r', encoding='utf-8') as line:

        lector_csv = csv.reader(line, delimiter='\t')

        for fila in lector_csv:
            # Se toma la clave y los valuees de cada fila
            key = fila[0]
            # Se divide cada fragmento jjj:numero
            aux = fila[4].split(',')
            # Se toma solo el numero de cada fragmento
            values = [int(value.split(':')[1]) for value in aux]
            # Se suman los valuees
            suma = sum(values)

            #
            # Si no esta en el diccionario, se agrega
            if key not in dict:
                dict[key] = suma
            else:
                dict[key] += suma

    return dict