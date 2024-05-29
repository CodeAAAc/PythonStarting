beatles = [];
print(beatles);

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print(beatles);

for i in range(2):
    nombre = input ("Ingrese el nombre del nuevo beatle: ");
    beatles.append(nombre);
print(beatles)

del beatles[3]
del beatles[3]

print(beatles)

beatles.insert(0,"Ringo Starr")
print(beatles)


print("Longitud de la lista", len(beatles))
