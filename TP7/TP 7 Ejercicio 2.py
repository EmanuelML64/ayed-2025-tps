def binario_a_decimal(binario: int,potencia = 0)->int:
    '''Convierte un numero binario a decimal multiplicando el ultimo digito del binario para luego sacarle el ult digito recursivamente.
    Precondiciones: recibe un entero como numero binario a convertir, la potencia a la cual multiplica es por defecto cero.
    Poscondiciones: devuelve el numero decimal'''
    if binario == 0:
        return 0
    ultimo = binario % 10
    return ultimo * (2**potencia) + binario_a_decimal(binario//10,potencia + 1)

numero = int(input("Ingrese el numero que quiere transformar de binario a decimal: "))
print(binario_a_decimal(numero))

