# TP Ejercicio 3
# Algoritmos y estructuras de datos
def cuadrados_de_la_lista(N):
    cuadrados = []
    for i in range(1,N):
        numero = i**2
        cuadrados.append(numero)
    return cuadrados

N = int(input("Ingrese el ultimo numero al cuadrado: "))

print(cuadrados_de_la_lista(N))