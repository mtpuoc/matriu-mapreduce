import functions
input = [("M1",1,1,2), ("M1",1,2,3), ("M1",1,3,4), ("M1",2,1,1), ("M1",2,2,0), ("M1",2,3,2), ("M1",3,1,3), ("M1",3,2,1), ("M1",3,3,1), ("M2",1,1,1), ("M2",1,2,0), ("M2",1,3,1), ("M2",2,1,0), ("M2",2,2,1), ("M2",2,3,0), ("M2",3,1,0), ("M2",3,2,0), ("M2",3,3,1)]

"PRIMERA PASADA"
list_map = functions.primer_map(input)

print("sortida map:", list_map)

list_reduce = functions.primer_reduce(list_map)

print("sortida reduce:", list_reduce)

print()

"SEGONA PASADA"

a = functions.segon_map(list_reduce)
print(a)
exit()

for item in list_reduce:
    index=0
    number_i = item[0]
    for subitem in item[1]:
        print(number_i, subitem)
        exit()
        if item[1][index][0] == "M1":
            print(number_i, item[1][index][1],item[1][index][2],item[1][index+3][2])
            "* item[1][index][1][3][2]"
            exit()



