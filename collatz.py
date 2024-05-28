numero = int(input("Ingresa un numero: "));
pasos = 0;

if numero <= 0:
    print ("El número no debe ser negativo ni igual a cero")
else:
    while True:
        if numero % 2 == 0:
            numero = numero // 2;

        else:
            numero = numero * 3 + 1;
        
        print(numero);
        pasos = pasos + 1;
        if numero == 1:
            break
            
print ("pasos: ", pasos)
