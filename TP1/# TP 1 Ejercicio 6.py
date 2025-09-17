# TP 1 Ejercicio 6
# Algoritmos y estructuras de datos
def concatenar(a:int, b:int) -> int:
    for i in range(len(str(b))-1, -1, -1): 
        a *= 10
        x = b // (10**i)
        a += x
        b -= x*(10**i)
    return a

print(concatenar(1234, 567))