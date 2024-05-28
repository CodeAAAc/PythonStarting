bloques = int(input("Ingresa el número de bloques: "));

bloques_por_nivel = 1;
niveles = 0;

while True:
    bloques = bloques - bloques_por_nivel;
    bloques_por_nivel = bloques_por_nivel + 1;

    if (bloques < 0): 
        break;
    
    niveles = niveles + 1;
    
print ("La pirámide tiene: "+ str(niveles) + " niveles");
