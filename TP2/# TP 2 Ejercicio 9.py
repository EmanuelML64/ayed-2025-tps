# TP 2 Ejercicio 9
# Algoritmos y estructura de datos
def multiplodelistas(A,B):
    listamult = [numero for numero in range(A,B) if numero % 7 == 0 and numero % 5 != 0]
    return listamult

a = int(input("Ingrese el limite inferior: "))
b = int(input("Ingrese el limite superior: "))
print(multiplodelistas(a,b))
