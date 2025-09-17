# TP 1 Ejercicio 2
# Algoritmos y estrucutas de datos
def fecha(d:int,m: int,a: int) -> bool:
    valido = True
    if d > 31:
        valido = False
    if m == 2 and d >= 30:
        valido = False
    if m < 1 or m > 12:
        valido = False
    if a > 2025:
        valido = False
    return valido
dia = int(input("Ingrese un dia: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))
comprobacion = fecha(dia,mes,anio)
print(comprobacion)
    