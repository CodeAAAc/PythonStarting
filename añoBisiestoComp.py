año = int(input("Introduce un año que quieres consultar: "))

if año < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:
    if año % 4 != 0:
        print("Año común")
    elif año % 100 != 0:
        print("Año bisiesto")
    elif año % 400 != 0:
        print("Año común")
    else:
        print("Año bisiesto")
