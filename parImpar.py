# Programa para contar números pares e impares
impares = 0
pares = 0

# Lee el primer número.
numero = int(input("Introduce un número o escribe 0 para detener: "))

# 0 termina la ejecución.
while numero != 0:
    # Verificar si el número es impar.
    if numero % 2 == 1:
        # Incrementar el contador de números impares odd_numbers.
        impares += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        pares += 1
    # Leer el siguiente número.
    numero = int(input("Introduce un número o escribe 0 para detener: "))

# Imprimir resultados.
print("Conteo de números impares:", impares)
print("Conteo de números pares:", pares)


