# TP 2 Ejercicio 7
# Algoritmos y estructuras de datos
def intercalar(lista1,lista2):
    nueva = []
    i = 0
    j = 0
    while i < len(lista1) and j < len(lista2):
        nueva.append(lista1[i])
        nueva.append(lista2[j])
        i += 1
        j += 1
    nueva.extend(lista1[i:])
    nueva.extend(lista2[j:])

    lista1[:] = nueva
    return lista1

listax = [8,1,3]
listay = [5,9,7]
print(intercalar(listax,listay))