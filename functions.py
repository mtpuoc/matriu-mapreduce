
def primer_map(input):
    list_m1 = []
    list_m2 = []
    for item in input:
        if item[0] == "M1":
            k = (item[1], (item[0], item[2], item[3]))
            list_m1.append(k)
        else:
            k = (item[2], (item[0], item[1], item[3]))
            list_m2.append(k)
    # print(list_m1)
    # print(list_m2)
    return list_m1 + list_m2

def primer_reduce(list_map):
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


def get_matriz(list_primer_reduce, name):
    matriz = dict()
    for item in list_primer_reduce:
        matriz[item[0]] = [i for i in item[1] if i[0] == name]
    return matriz


def segon_map(list_primer_reduce):
    list_first_matriz = get_matriz(list_primer_reduce, "M1")
    list_second_matriz = get_matriz(list_primer_reduce, "M2")

    index = 1
    for key, value in list_first_matriz.items():
        print(key)
        for i, value_first in enumerate(value):
            exit()

    list_segon_map = []
    index = 1
    for item in list_primer_reduce:
        #print(item[0], index)
        for i, subitem in enumerate(item[1]):
            if subitem[0] == "M1":
                t = ((item[0], index), subitem[2]*item[1][i+3][2])
                list_segon_map.append(t)
    print(list_segon_map)

segon_map([(1, [('M1', 1, 2), ('M1', 2, 3), ('M1', 3, 4), ('M2', 1, 1), ('M2', 2, 0), ('M2', 3, 0)]), (2, [('M1', 1, 1), ('M1', 2, 0), ('M1', 3, 2), ('M2', 1, 0), ('M2', 2, 1), ('M2', 3, 0)]), (3, [('M1', 1, 3), ('M1', 2, 1), ('M1', 3, 1), ('M2', 1, 1), ('M2', 2, 0), ('M2', 3, 1)])])