import generarDatos
fechas = set()

for i in range(1000):
    fechas.add(generarDatos.diaRandom(2,1900))

print(fechas)