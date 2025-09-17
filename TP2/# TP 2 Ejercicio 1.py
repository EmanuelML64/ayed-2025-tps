# TP 2 Ejercicio 1
# Algoritmos y estructuras de datos
import random
def imprimir_lista(lista):
    for elemento in lista:
        print(elemento, end = " ")

def lista_al_azar():
    lista_azar = []
    cantidad = random.randint(10,99)
    for i in range(cantidad):
        numero = random.randint(1000,9999)
        lista_azar.append(numero)
    return lista_azar

ejemplo = lista_al_azar()
print(ejemplo)

imprimir_lista(ejemplo)


def producto_lista(lista):
    producto = 1
    for elemento in lista:
        producto *= elemento
    return producto

print()
print(producto_lista(ejemplo))


def eliminar_valor(borrar,lista):
    for elemento in lista:
        if borrar == elemento:
            lista.remove(elemento)
    return lista

eliminar = int(input("Ingrese el elemento de la lista a borrar: "))
print(eliminar_valor(eliminar,ejemplo))

def es_capicua(lista):
    return lista == lista[::-1]

example1 = [1,5,7,5,1]
example2 = [1,2,3,4,5]

print(es_capicua(example1))
print(es_capicua(example2))
