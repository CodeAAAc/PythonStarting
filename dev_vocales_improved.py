user_word = input ("Ingrese una palabra clave: ")
user_word = user_word.upper()

word_without_vowels = ""


for y in user_word:
    if y == "A":
        continue
    elif y == "E":
        continue
    elif y == "I":
        continue
    elif y == "O":
        continue
    elif y == "U":
        continue
    else: 
        word_without_vowels = word_without_vowels + y
        
print (word_without_vowels)
