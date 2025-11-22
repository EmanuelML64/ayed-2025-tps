def multiplicachion(a:int,b:int)->int:
    '''Multiplica 4 X 3 haciendo 4 + 4 + 4
    Precondiciones: recibe los dos numeros enteros a multiplicar
    Poscondiciones: devuelve el resultado de la multiplicacion de los numeros.'''
    if b == 0:
        return 0
    return a + multiplicachion(a,b - 1)

numerin = int(input("Ingrese el primer numero a multiplicar: "))
numerote = int(input("Ingrese el segundo numero a multiplicar: "))
print(multiplicachion(numerin,numerote))

