secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
mugle_number = int(input("Dime el número secreto: "))

while mugle_number != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    mugle_number = int(input("Dime el número secreto: "))
    
print("¡Bien hecho, muggle! Eres libre ahora.")
