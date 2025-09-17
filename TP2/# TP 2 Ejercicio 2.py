# TP 2 Ejercicio 2
# Algoritmos y estructuras de datos
import random
def numeros_aleatorios():
    lista_aleatoria = []
    cantidad = int(input("Ingrese la cantidad de elementos que quiere en la lista: "))
    for i in range(cantidad):
        numero = random.randint(1,100)
        lista_aleatoria.append(numero)
    return lista_aleatoria

print(numeros_aleatorios())

def elemento_repetido(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

lista1 = [1,2,1,3]
lista2 = [1,2,3,4]

print(elemento_repetido(lista1))
print(elemento_repetido(lista2))


def lista_original(lista):
    nueva_lista = []
    for elemento in lista:
        if elemento not in nueva_lista:
            nueva_lista.append(elemento)
    return nueva_lista




liston = [1,3,3,5,5,5,5,7,7,2,2,3,3,2,4,4,5]
print(lista_original(liston))


