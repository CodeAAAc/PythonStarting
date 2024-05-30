my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

my_list2 = my_list[:]
my_list3 =[]

for i in range(len(my_list2)):
    for j in range(len(my_list2[i+1:])):
        if my_list2[i] == my_list2[i+j+1]:
            my_list2[j+1] = 0
        
print("La lista con elementos únicos:")
print(my_list2)
