# TP 1 Ejercicio 4
# Algoritmos y estructuras de datos
def vuelto(total: int, recibido: int) -> list:
    if total > recibido:
        return [-1]
    # Crea una lista de 7 elementos en cero
    billetes = []
    # Calculo lo que debe devolver
    devolver = recibido - total
    for v in valores:
        billetes.append(devolver//v)
        devolver %= v     # Guardo el resto de la division
    return billetes

valores = [500,100,50,20,10,5,2,1]
pago = 496
billete = 1000
if pago > billete:
    print("No alcanza para hacer el pago")
else:
    salida = vuelto(pago,billete)
    # Uso de enumerate para las listas
    for i,s in enumerate(salida): # Ver enumerate
        if s:    # Revisa si es verdadero o falso, tomando 1 como True y 0 como False. Es lo mismo que s != 0
            print(f"{s} billetes de {valores[i]}")
# Enumerate devuelve una tupla con (indice,valor), elemento inmutable e iterable
# El desempaquetado de datos seria asi: indice,dato = (0,500)
# print(indice): 0
# print(dato): 500
# Tambien se puede usar divmod(a,b), devolviendo una tupla (a//b),(a%b)