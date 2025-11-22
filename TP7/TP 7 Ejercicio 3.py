def suma_factorial(n:int)->int:
    '''Calcula la suma de todos los numeros anteriores a un numero n.
    Precondiciones: Recibe el numero mas alto el cual va a sumar todos sus anteriores hasta llegar a cero.
    Poscondiciones: devuelve la sumatoria de los numeros factorialmente.'''
    if n == 1:
        return 1
    return n + suma_factorial(n - 1)


numerito = int(input("Ingrese el numero del cual quiere sumar sus anteriores: "))
print(suma_factorial(numerito))

