
import csv

def pregunta_11():

    route = "files/input/data.csv"
    # diccionario que almacena los registros
    dict = {}

    with open(route, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
        
        for fila in lector_csv:
            # Obtenemos las letra de la columna 4, y se itera sobre ellos
            letters__col4 = fila[3].split(',')

            for letter in letters__col4:
                # Si no exta en el diccionario, se agrega
                if letter not in dict:
                    dict[letter] = int(fila[1])
                else:
                    dict[letter] += int(fila[1])
    
    return dict