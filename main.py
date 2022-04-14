import functions

input = [("M1",1,1,2), ("M1",1,2,3), ("M1",1,3,4), ("M1",2,1,1), ("M1",2,2,0), ("M1",2,3,2), ("M1",3,1,3), ("M1",3,2,1), ("M1",3,3,1), ("M2",1,1,1), ("M2",1,2,0), ("M2",1,3,1), ("M2",2,1,0), ("M2",2,2,1), ("M2",2,3,0), ("M2",3,1,0), ("M2",3,2,0), ("M2",3,3,1)]

"PRIMERA PASADA"

list_map = functions.primer_map(input)

print("1. salida map:", list_map)

list_shuffle = functions.primer_shuffle(list_map)

print("2. salida shuffle:", list_shuffle)

"Al no poder aplicar el reduce ya que no hay valores para sumar, no se crear ninguna función"

print()

"SEGONA PASADA"

segona_pasada_map = functions.segon_map(list_shuffle)

print("3. salida segunda pasada map:", segona_pasada_map)

segon_shuffle = functions.segon_shuffle(segona_pasada_map)

print("4. salida segunda pasada shuffle:",segon_shuffle)

output = functions.segon_reduce(segon_shuffle)

print("5. salida segunda pasada reduce:",output)

assert output == [((1,1),2),((1,2),3),((1,3),6),((2,1),1),((2,2),0),((2,3),3),((3,1),3),((3,2),1),((3,3),4)]

print("OK")

