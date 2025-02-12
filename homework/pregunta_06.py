import csv

def pregunta_06():

    route = "files/input/data.csv"
    # diccionario que almacena los registros
    dict = {}

    with open(route, 'r', encoding='utf-8') as file:
        lector_csv = csv.reader(file, delimiter='\t')

        for fila in lector_csv:

            # Se toma una linea de la columna 5
            string= fila[4]

            # Se divide la cadena, separa por comas
            datos = string.split(',')
            
            #
            # Se itera sobre cada uno de los datos separados
            #
            for dato in datos:
                # Se separan en pares de clave valor
                key, value = dato.split(':')
                value = int(value)
                

                # Si no esta en el diccionario, se crea
                if key not in dict:
                    dict[key] = [value, value]

                # Si esta, se comprueban sus tuplas para tomar valores máximos y minimos

                else:
                    if value <= dict[key][0]:
                        dict[key][0] = value

                    elif value >= dict[key][1]:
                        dict[key][1] = value

    # Retorna en el orden pedido
    # En onde se mete, que se mete, ciclo for
    lista = [(key, value[0], value[1]) for key, value in sorted(dict.items())]
    
    return lista

