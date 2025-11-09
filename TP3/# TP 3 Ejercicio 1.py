# TP 3 Ejercicio 1
from typing import List
import random
def cargar_matriz() -> list[list[int]]:
    '''Carga una matriz con numeros aleatorios entre 0 y 1000. El usuario elige la cantidad de filas
    y columnas.
    Precondiciones: Debe ingresarse un numero entero para expresar la cantidad de filas y la cantidad
    de columnas.
    Poscondiciones: Devuelve una matriz de numeros enteros'''
    filas = int(input("Ingrese la cantidad de filas de la matriz: "))
    columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))
    matriz = [[random.randint(0,1000)for j in range (columnas)] for i in range(filas)]
    return matriz

matrix = (cargar_matriz())
print(matrix)

def ordenar_matriz(matriz: list[list]) -> list[list]:
    '''Ordena la matriz de forma ascendente.
    Precondiciones: matriz numerica
    Poscondiciones: devuelve una matriz numerica ordenada'''
    return [sorted(fila) for fila in matriz]

print(ordenar_matriz(matrix))

def intercambiar_filas(matriz: list[list],fila1: int,fila2: int) -> list[list]:
    '''Intercambia las filas de la matriz, poniendo una fila en lugar de la otra.
    Precondiciones: la matriz debe ser numerica. Las filas deben ser numeros enteros.
    Poscondiciones: matriz con las filas intercambiadas'''
    matriz[fila1],matriz[fila2] = matriz[fila2],matriz[fila1]
    return matriz

print(intercambiar_filas(matrix,0,1))


def intercambiar_columnas(matriz: list[list], columna1: int, columna2: int) -> list[list]:
    '''Intercambia las columnas de una matriz colocando una en lugar de la otra.
    Precondiciones: matriz numerica, enteros para representar las columnas.
    Poscondiciones: matriz con las columnas intercambiadas'''
    for fila in matriz:
        fila[columna1],fila[columna2] = fila[columna2],fila[columna1]
    return matriz

print(intercambiar_columnas(matrix,1,2))

def matriz_traspuesta(matriz: list[list]) -> list[list]:
    '''Traspone la matriz. Las filas se transforman en columnas y las columnas en filas.
    Precondiciones: matriz numerica.
    Poscondiciones: matriz traspuesta'''
    return [[fila[i]for fila in matriz]for i in range(len(matriz[0]))]

print(matriz_traspuesta(matrix))

def promedio_fila(matriz: list[list],fila: int)->float:
    '''Calcula el promedio de una fila determinada.
    Precondiciones: matriz numerica, numero entero para representar la fila a calcular.
    Poscondiciones: devuelve un numero real representando el cociente de la sumatoria de los
    valores de la fila y la cantidad de valores en la fila'''
    return(sum(matriz[fila])/len(matriz[fila]))

def impar_columna(matriz: list[list],columna: int)->float:
    '''Calcula el porcentaje de valores impares en una columna.
    Precondiciones: matriz numerica y numero entero para representar la columna.
    Poscondiciones: devuelve un numero real que indica el porcentaje de impares.'''
    valores = [fila[columna]for fila in matriz]
    impares = [valor for valor in valores if valor % 2 != 0]
    percentage = (len(impares)/len(valores))*100
    return percentage,"%"

print(impar_columna(matrix,1))

def simetrica_principal(matriz: list[list])-> bool:
    '''Verifica si una matriz es simetrica con respecto a su diagonal principal.
    Precondiciones: matriz numerica.
    Poscondiciones: valor booleano indicando si es simetrica o no '''
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):
            if matriz[i][j] != matriz[j][i]:
                return False, "Asimetrica a su diagonal principal"
    return True, "Simetrica a su diagonal principal"

print(simetrica_principal(matrix))

def simetrica_secundaria(matriz: list[list]) -> bool:
    '''Verifica si una matriz es simetrica con respecto a su diagonal secundaria.
    Precondiciones: matriz numerica.
    Poscondiciones: valor booleano indicando si es simetrica o no '''
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] != matriz [len(matriz) - 1 - j][len(matriz) - 1 - i]:
                return False, "Asimetrica a su diagonal secundaria"
    return True, "Simetrica a su diagonal secundaria"

print(simetrica_secundaria(matrix))

def capicua(matriz: list[list]) -> list[int]:
    filas = len(matriz)
    columnas = len(matriz[0])
    capicuas = []
    for j in range(columnas):
        col = [matriz[i][j] for i in range(filas)]

        if col == col[::-1]:
            capicuas.append(j + 1)
    return capicuas

print(capicua(matrix))


            