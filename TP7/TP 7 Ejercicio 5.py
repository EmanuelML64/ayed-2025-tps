def resto(a:int,b:int)->int:
    '''Obtiene el resto de la division restando sucesivamente.
    Precondiciones: recibe dos numeros enteros, dividendo y divisor.
    Poscondiciones: devuelve el resto de la division.'''
    if a < b:
        return a
    return resto(a - b,b)

dividendo = int(input("Ingrese el numero a dividir: "))
divisor = int(input("Ingrese el numero que divide: "))
print(resto(dividendo,divisor))
