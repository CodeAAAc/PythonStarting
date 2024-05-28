print("Programador devorador de vocales")
user_word = input("Ingrese una palabra clave: ")
user_word = user_word.upper()

for x in user_word:
    if x == "A":
        continue
    elif x == "E":
        continue
    elif x == "I":
        continue
    elif x == "O":
        continue
    elif x == "U":
        continue
    else:
        print (x)
