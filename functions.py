"""
Se crean las tuplas para poder agruparlas, teniendo en cuenta que la Matriz para que sea clave de M1 es "i" i M2 es "j".
"""
def primer_map(input):
    list_m1 = [(item[1], (item[0], item[2], item[3])) for item in input if item[0]=="M1"]
    list_m2 = [(item[2], (item[0], item[1], item[3])) for item in input if item[0]=="M2"]
    # print(list_m1)
    # print(list_m2)
    return list_m1 + list_m2

"""
Se agrupan las tuplas por las claves que coinciden, en este punto no se puede utilizar un reduce ya que no hay ninguna operación para sumar.
"""
def primer_shuffle(list_map):
    dict_reduce = dict()
    while len(list_map) > 0:
        item = list_map.pop(0)
        if item[0] in dict_reduce:
            items = dict_reduce[item[0]]
            items.append(item[1])
            dict_reduce[item[0]] = items.copy()
        else:
            dict_reduce[item[0]] = [item[1]]
    list_reduce = [(index, value) for index, value in dict_reduce.items()]
    return list_reduce

"""
Función para ayudar en la segunda pasada del map: Para separar los registros de las tuplas de M1 y M2
"""
def _get_matriz(list_primer_reduce, name):
    matriz = dict()
    for item in list_primer_reduce:
        matriz[item[0]] = [i for i in item[1] if i[0] == name]
    return matriz

"""
Se crean las tuplas para aplicar la funcionalidad de la matriz producto, donde se multipla cada posición de M1 horizontal por M2 vertical de cada elemento.
Primer elemento de M1 hay que multipar para cada M2 y asi para la resta de elementos, por eso incluye un doble for.
"""
def segon_map(list_primer_reduce):
    list_first_matriz = _get_matriz(list_primer_reduce, "M1")
    list_second_matriz = _get_matriz(list_primer_reduce, "M2")

    list_segon_map = []
    for key, value in list_first_matriz.items():
        #print(key)
        for k, value_second in list_second_matriz.items():
            list_segon_map.append(((key,k), value[0][2] * value_second[0][2]))
            list_segon_map.append(((key,k), value[1][2] * value_second[1][2]))
            list_segon_map.append(((key,k), value[2][2] * value_second[2][2]))
    #print(list_segon_map)
    return list_segon_map

"""
Se agrupa las tuplas con los elementos que tienen el mismo valor, al generar la salida del segundo map, los registros estan alineados asi que no se aplica ningun orden.
"""
def segon_shuffle(segon_map):
    list_segon = []
    while len(segon_map) > 0:
        item_1 = segon_map.pop(0)
        item_2 = segon_map.pop(0)
        item_3 = segon_map.pop(0)
        list_segon.append((item_1[0],[item_1[1],item_2[1],item_3[1]]))
    return list_segon

"""
Se realiza la función de reduce donde se suma los valors de la lista.
"""
def segon_reduce(segon_shuffle):
    return [(i[0], sum(i[1])) for i in segon_shuffle]

