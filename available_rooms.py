rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
rooms[1][9][13] = True

rooms[2][14][3] = True
vacancy = 0
 
for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1


print(rooms)
print("El número de habitaciones disponibles en el edif 3, piso 15 es: ", vacancy)
