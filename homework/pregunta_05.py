import csv

def pregunta_05():
    route = "files/input/data.csv"
    # Diccionario que almacena los registros
    dict = {}
    with open(route, 'r', encoding='utf-8') as file:
        lector_csv = csv.reader(file, delimiter='\t')
        for fila in lector_csv:
            # Se toma la letra de la col 1, y el numero de la col 2
            letter = fila[0]
            number = int(fila[1])

            # Si no esta en el diccionario, se crea
            if letter not in dict:
                dict[letter] = [number, number]

            # Si esta, se comprueban sus tuplas para tomar valores máximos y minimos
            else:
                if number >= dict[letter][0]:
                    dict[letter][0] = number

                elif number <= dict[letter][1]:
                    dict[letter][1] = number

    # Retorna en el orden pedido
    # En onde se mete, que se mete, ciclo for
    lista = [(clave, valor[0], valor[1]) for clave, valor in sorted(dict.items())]
    
    return lista
   
