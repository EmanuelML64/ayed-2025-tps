# TP 2 Ejercicio 10
# Algoritmos y estructura de datos
import random
listarandom = []
for i in range(11):
    numero = random.randint(1,100)
    listarandom.append(numero)
print(listarandom)
def es_impar(x):
    return x % 2 != 0

impares = list(filter(es_impar,listarandom))
print(impares)
