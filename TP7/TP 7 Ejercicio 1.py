def cantidad_digitos(n: int)->int:
    '''Cuenta la cantidad de digitos de un numero.
    Precondiciones: recibe un numero entero por teclado.
    Poscondiciones: Devuelve un numero entero representando la cantidad de digitos del numero.'''
    n = abs(n)
    if n < 10:
        return 1
    return 1 + cantidad_digitos(n//10)

numero = int(input("Ingrese el numero para contar sus digitos: "))
print(cantidad_digitos(numero))