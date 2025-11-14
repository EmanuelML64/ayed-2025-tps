# TP 3 Ejercicio 5
import random

def cargar_sala(N:int, M:int)->list[list]:
    '''
    Carga una sala de cine con valores aleatorios 0 o 1.
    Precondición: N y M deben ser enteros positivos.
    Poscondición: Retorna una matriz de tamaño N x M con 0 (libre) o 1 (ocupado).
    '''
    return [[random.choice([0, 1]) for _ in range(M)] for _ in range(N)]

def mostrar_butacas(sala: list[list])->None:
    '''
    Muestra por pantalla el estado actual de la sala.
    Precondición: sala debe ser una matriz de enteros 0 (libre) o 1 (ocupado).
    Poscondición: Imprime la sala sin modificarla.
    '''
    print("\nEstado de la sala:")
    for fila in sala:
        print(" ".join(str(b) for b in fila))
    print()

def reservar(sala:list[list], fila:int, butaca:int)->bool:
    '''
    Intenta reservar una butaca en la sala.
    Precondición: sala debe ser una matriz válida; fila y butaca deben estar dentro de rango.
    Poscondición: Si la butaca está libre (0), se marca como ocupada (1) y devuelve True.
    Si ya estaba ocupada, devuelve False.
    '''
    if sala[fila][butaca] == 0:
        sala[fila][butaca] = 1
        return True
    return False

def butacas_libres(sala:list[list])->int:
    '''
    Cuenta cuántas butacas libres hay en la sala.
    Precondición: sala debe ser una matriz de 0 y 1.
    Poscondición: Retorna la cantidad de butacas libres (valores 0).
    '''
    return sum(b == 0 for fila in sala for b in fila)

def butacas_contiguas(sala:list[list])->tuple:
    '''
    Busca la secuencia más larga de butacas contiguas libres en una misma fila.
    Precondición: sala debe ser una matriz rectangular de 0 y 1.
    Poscondición: Retorna una tupla (longitud, (fila, columna_inicio)).
    Si no hay butacas libres, retorna (0, (-1, -1)).
    '''
    mejor = (0, (-1, -1))
    for i, fila in enumerate(sala):
        cont = 0
        inicio = 0
        for j, b in enumerate(fila + [1]):
            if b == 0:
                cont += 1
            else:
                if cont > mejor[0]:
                    mejor = (cont, (i, inicio))
                cont = 0
                inicio = j + 1
    return mejor


N = int(input("Filas: "))
M = int(input("Butacas por fila: "))

sala = cargar_sala(N, M)
mostrar_butacas(sala)

fila = int(input("Elegí la fila : "))
butaca = int(input("Elegí la butac: "))

if reservar(sala, fila, butaca):
    print("\nReserva realizada con éxito")
else:
    print("\nEsa butaca ya está ocupada")

mostrar_butacas(sala)

print(f"Butacas libres: {butacas_libres(sala)}")
longitud, (f, c) = butacas_contiguas(sala)
print(f"Mayor secuencia libre: {longitud} butacas seguidas (fila {f}, desde columna {c})")
