# TP 3 ejercicio 4
import random

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
N = int(input("Ingrese la cantidad de fábricas: "))

matriz = [[random.randint(0, 150) for _ in dias] for _ in range(N)]

print("\nProducción semanal (filas=fábricas / columnas=días):\n")
for i, fila in enumerate(matriz, 1):
    print(f"Fábrica {i}: {fila}")

# a) Total por fábrica
totales_fabrica = [sum(f) for f in matriz]
print("\nTotal por fábrica:", totales_fabrica)

# b) Total por día
totales_dia = [sum(matriz[i][j] for i in range(N)) for j in range(len(dias))]
print("Total por día:", dict(zip(dias, totales_dia)))

# c) Fábrica y día con mayor producción
maximo = 0
fab_max = dia_max = 0
for i in range(N):
    for j in range(len(dias)):
        if matriz[i][j] > maximo:
            maximo = matriz[i][j]
            fab_max, dia_max = i, j
print(f"\nMayor producción: {maximo} bicicletas (Fábrica {fab_max+1}, {dias[dia_max]})")

# d) Día con mayor producción total (todas las fábricas)
dia_mas = dias[totales_dia.index(max(totales_dia))]
print(f"Día con más producción total: {dia_mas}")

# e) Menor cantidad fabricada por fábrica
menores = [min(f) for f in matriz]
print("Menor cantidad por fábrica:", menores)
