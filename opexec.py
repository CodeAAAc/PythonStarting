print ("Programa que recibe la hora actual, la duración de evento, y devuelve la hora de finalización del evento")

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

hours = (mins + dura) // 60 + hour
mins2 = (mins + dura) % 60
print (hours, mins2, sep=":")
