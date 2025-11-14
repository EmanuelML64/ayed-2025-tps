# TP 3 Ejercicio 3
import random

N = int(input("Ingrese el tamaño N de la matriz: "))
nums = random.sample(range(0, N**2 + 1), N * N)
matriz = [nums[i * N:(i + 1) * N] for i in range(N)]

for fila in matriz:
    print(*fila)
