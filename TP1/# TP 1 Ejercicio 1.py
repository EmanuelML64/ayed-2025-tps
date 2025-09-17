# TP 1 Ejercicio 1 
# Algoritmos y estructuras de datos
def mayor(num1: int,num2: int,num3: int) ->int:
    if num1 > num2 and num1 > num3:
        maximo = num1
    if num2 > num1 and num2 > num3:
        maximo = num2
    if num3 > num1 and num3 > num2:
        maximo = num3
    else:
        return -1
    apariciones = 0
    if maximo == num1:
        apariciones += 1
    if maximo == num2:
        apariciones += 1
    if maximo == num3:
        apariciones += 1

    if apariciones == 1:
        return maximo
    else:
        return -1
    
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
num3 = int(input("Ingrese otro numero: "))

resultado = mayor(num1,num2,num3)
if resultado == -1:
    print("No hay un mayor estricto")
else:
    print("El mayor es: ", resultado)
