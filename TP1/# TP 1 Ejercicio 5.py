# TP 1 Ejercicio 5
# Algoritmos y estructuras de datos
es_oblongo = lambda n: any(i * (i + 1) == n for i in range(1, n))
print(es_oblongo(6))
print(es_oblongo(5))


es_triangular = lambda n: any(i*(i+1)//2 == n for i in range(1, n+1))
print(es_triangular(10))
print(es_triangular(9))
