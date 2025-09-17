# TP 2 Ejercicio 4
# Algoritmos y estructuras de datos
lista_original = [1,4,8,5,7,9,2,3,2,4,5]
lista_duplicada = [1,8,7,2]
a_eliminar = []
for elemento in lista_original:
    if elemento in lista_duplicada:
        a_eliminar.append(elemento)
        lista_original.remove(elemento)
print(lista_original)
print(f"Borrados {a_eliminar}")
