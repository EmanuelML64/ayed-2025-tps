# Trabajo practico 2 de algoritmos y estructuras de datos
# 1
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

# 2
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



# 3
def cuadrados_de_la_lista(N):
    cuadrados = []
    for i in range(1,N):
        numero = i**2
        cuadrados.append(numero)
    return cuadrados

N = int(input("Ingrese el ultimo numero al cuadrado: "))

print(cuadrados_de_la_lista(N))

# 4
lista_original = [1,4,8,5,7,9,2,3,2,4,5]
lista_duplicada = [1,8,7,2]
a_eliminar = []
for elemento in lista_original:
    if elemento in lista_duplicada:
        a_eliminar.append(elemento)
        lista_original.remove(elemento)
print(lista_original)
print(f"Borrados {a_eliminar}")

# 5 
def lista_ordenada(lista):
    return lista == sorted(lista)

listaorden = [1,2,3,4,5]
listadesorden = [2,1,4,2,5,3]
print(lista_ordenada(listaorden))
print(lista_ordenada(listadesorden))

# 6
def normalizar(lista):
    suma = sum(lista)
    return [elemento/suma for elemento in lista]



lista1 = [1,2,2]
lista2 = [3,3,4]
print(normalizar(lista1))
print(normalizar(lista2))

# 7
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

# 8 
impares = [numero for numero in range(100,200) if numero % 2 != 0]
imprimir_lista(impares)
print()
# 9
def multiplodelistas(A,B):
    listamult = [numero for numero in range(A,B) if numero % 7 == 0 and numero % 5 != 0]
    return listamult

a = int(input("Ingrese el limite inferior: "))
b = int(input("Ingrese el limite superior: "))
print(multiplodelistas(a,b))

# 10
listarandom = []
for i in range(11):
    numero = random.randint(1,100)
    listarandom.append(numero)
print(listarandom)
def es_impar(x):
    return x % 2 != 0

impares = list(filter(es_impar,listarandom))
print(impares)

# 11
pacientesconturno = []
pacientesconurgencias = []
afiliado = int(input("Ingrese sus cuatro digitos de numero de afiliado: "))
while afiliado != -1:
    nivel = int(input("Ingrese 0 para urgencias o 1 si viene con turno: "))
    if nivel == 0:
        pacientesconurgencias.append(afiliado)
    else:
        pacientesconturno.append(afiliado)
    afiliado = int(input("Ingrese su numero de afiliado: "))
print("Con turno: ",pacientesconturno)
print("Con urgencias: ",pacientesconurgencias)

encontradoconturno = 0
encontradoconurgencias = 0
busqueda = int(input("Ingrese un numero de afiliado a buscar: "))
while busqueda != -1:
    for paciente in pacientesconturno:
        if busqueda == paciente:
            encontradoconturno += 1
    for patient in pacientesconurgencias:
        if busqueda == patient:
            encontradoconurgencias += 1
print("Con turno:", encontradoconturno)
print("Con urgencias: ",encontradoconurgencias)

# 12
socios = []
numero = int(input("Ingrese el numero de socio, 5 digitos: "))
while numero != 0:
    socios.append(numero)

socio = []
cantidad = []

for soc in socios:
    if soc not in socio:
        socio.append(soc)

for soc in socio:
    cantidad.append(socios.count(soc))

for soc,cant in zip(socio,cantidad):
    print(f"El socio {soc} tuvo {cant} ingresos al club")

print("Ingresos: ")
print(cantidad)

baja = int(input("Ingrese el numero de socio a eliminar: "))
if baja in socios:
    for i in range(socios.count(baja)):
        socios.remove(baja)
else:
    print("Codigo de socio no valido")

print("La nueva lista es: ")
print(socios)

