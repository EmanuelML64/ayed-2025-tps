# TP 2 Ejercicio 6
# Algoritmos y estructura de datos
def normalizar(lista):
    suma = sum(lista)
    return [elemento/suma for elemento in lista]



lista1 = [1,2,2]
lista2 = [3,3,4]
print(normalizar(lista1))
print(normalizar(lista2))
