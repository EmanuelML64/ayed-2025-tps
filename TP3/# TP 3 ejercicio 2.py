# TP 3 ejercicio 2


def matriz_a(N:int)->list[list]:
    '''Genera una matriz donde la diagonal principal muestra numeros impares
    Precondicion: recibe un numero para saber las dimensiones de la matriz.
    Poscondicion: matriz con diagonal de impares.'''
    m = [[0]*N for _ in range(N)]
    for i in range(N):
        m[i][i] = 2*i + 1
    return m

def matriz_b(N:int)->list[list]:
    '''Genera una matriz con su diagonal secundaria cubierta por numeros multiplos del 3 hasta
    el numero 1.
    Precondiciones: numero entero para las dimensiones de la matriz.
    Poscondiciones: matriz con diagonal secundaria de multiplos de 3.'''    
    m = [[0]*N for _ in range(N)]
    for i in range(N):
        m[i][N-1-i] = 3**(N-1-i)
    return m

def matriz_c(N:int)->list[list]:
    '''Genera una matriz de arriba a abajo con cada numero correspondiente a su numero de fila.
    Precondiciones: numero entero para las dimensiones de la matriz.
    Poscondiciones: matriz de numeros descendentes que aumentan en cantidad por fila.'''
    m = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if j <= i:
                m[i][j] = N - i
    return m

def matriz_d(N:int)->list[list]:
    '''Genera las potencias de dos arrancando desde uno de abajo para arriba.
    Precondiciones: numero entero para medir las dimensiones de la matriz.
    Poscondiciones: matriz de potencias de 2 de abajo para arriba.'''
    m = [[0]*N for _ in range(N)]
    for i in range(N):
        val = 2**(N-1-i)
        for j in range(N):
            m[i][j] = val
    return m

def matriz_e(N:int)->list[list]:
    '''Genera una matriz intercalando numeros con un cero entremedio.
    Precondiciones: numero entero para determinar las dimensiones de la matriz.
    Poscondiciones: devuelve una matriz con numeros intercalados por el cero.'''
    m = [[0]*N for _ in range(N)]
    cnt = 1
    for i in range(N):
        for j in range(N):
            if (i + j) % 2 == 1:
                m[i][j] = cnt
                cnt += 1
    return m

def matriz_f(N:int)->list[list]:
    '''Genera una matriz de numeros que aumentan de derecha a izquierda, aumentando una columna mas
    a la derecha cada vez que desciende una fila.
    Precondiciones: numero entero para determinar las dimensiones de la matriz.
    Poscondiciones: matriz de numeros que aumentan de derecha a izquierda.'''
    m = [[0]*N for _ in range(N)]
    cnt = 1
    for i in range(N):
        
        for j in range(N-1, N-2-i, -1):
            m[i][j] = cnt
            cnt += 1
    return m

def matriz_g(N:int)->list[list]:
    '''Genera una matriz que aumenta en espiral.
    Precondiciones: recibe un numero entero para determinar las dimensiones de la matriz.
    Poscondiciones: devuelve una matriz de numeros que aumentan en forma de espiral.'''
    m = [[0]*N for _ in range(N)]
    top, bottom, left, right = 0, N-1, 0, N-1
    cnt = 1
    while top <= bottom and left <= right:
        for j in range(left, right+1):
            m[top][j] = cnt; cnt += 1
        top += 1
        for i in range(top, bottom+1):
            m[i][right] = cnt; cnt += 1
        right -= 1
        if top <= bottom:
            for j in range(right, left-1, -1):
                m[bottom][j] = cnt; cnt += 1
            bottom -= 1
        if left <= right:
            for i in range(bottom, top-1, -1):
                m[i][left] = cnt; cnt += 1
            left += 1
    return m

def matriz_h(N:int)->list[list]:
    '''Genera una matriz de numeros que aumentan en forma de diagonales secundarias.
    Precondiciones: recibe un entero para determinar las dimensiones de la matriz.
    Poscondiciones: Devuelve una matriz que aumenta como diagonales secundarias de derecha a izquierda.'''
    m = [[0]*N for _ in range(N)]
    cnt = 1
    for s in range(0, 2*N - 1):
        for i in range(N):
            j = s - i
            if 0 <= j < N:
                m[i][j] = cnt
                cnt += 1
    return m

def matriz_i(N:int)->list[list]:
    '''Genera una matriz que aumenta en zigzag.
    Precondiciones: recibe un entero que determina las dimensiones de la matriz.
    Poscondiciones: devuelve una matriz que aumenta en zigzag.'''
    m = [[0]*N for _ in range(N)]
    cnt = 1
    for s in range(0, 2*N - 1):
        positions = [(i, s - i) for i in range(N) if 0 <= s - i < N]
        if s < 2:
            order = positions
        else:
            
            order = list(reversed(positions)) if (s % 2 == 0) else positions
        for (ii, jj) in order:
            m[ii][jj] = cnt
            cnt += 1
    return m

def imprimir(m:list[list])->list[list]:
    '''Imprime la matriz.
    Precondicion: matriz a imprimir.
    Poscondicion: matriz impresa'''
    for fila in m:
        print(" ".join(f"{x:3}" for x in fila))
    print()

if __name__ == "__main__":
    N = int(input("Ingresa el tamaño N de la matriz: "))
    funcs = {
        'a': matriz_a, 'b': matriz_b, 'c': matriz_c,
        'd': matriz_d, 'e': matriz_e, 'f': matriz_f,
        'g': matriz_g, 'h': matriz_h, 'i': matriz_i
    }
    for clave, func in funcs.items():
        print(f"Matriz {clave}:")
        imprimir(func(N))
