# TP 2 Ejercicio 5
# Algoritmos y estructura de datos
def lista_ordenada(lista):
    return lista == sorted(lista)

listaorden = [1,2,3,4,5]
listadesorden = [2,1,4,2,5,3]
print(lista_ordenada(listaorden))
print(lista_ordenada(listadesorden))
