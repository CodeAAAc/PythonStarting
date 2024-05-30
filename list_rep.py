my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

print("La lista inicial");
print(my_list);

my_list2 = []
long_list = len(my_list);

sw = True

for i in range(long_list):
    for j in range(i):
        if my_list[i] == my_list[j]:
            sw = False
            break
        else:
            sw = True
    if sw:
        my_list2.append(my_list[i])
        
print("La lista con elementos únicos:")
print(my_list2)
