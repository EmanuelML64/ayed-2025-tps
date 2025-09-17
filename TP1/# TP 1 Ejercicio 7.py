# TP 1 Ejercicio 7
# Algoritmos y estructuras de datos
def diasiguiente(dia,mes,anio):
    if dia == 31 and mes == 12:
        diasig = 1
        messig = 1
        aniosig = anio + 1
    elif dia == 31 and mes > 0 and mes < 12:
        diasig = 1
        messig = mes + 1
        aniosig = anio
    else:
        diasig = dia + 1
        messig = mes
        aniosig = anio
    return diasig,messig,aniosig

day = int(input("Ingrese el dia a comprobar: "))
month = int(input("Ingrese el mes a comprobar: "))
year = int(input("Ingrese el año a comprobar: "))
sigday = diasiguiente(day,month,year)
print(sigday)

# Sumar N dias
n = int(input("Ingrese la cantidad de dias a sumar: "))
for i in range(n):
    day,month,year = diasiguiente(day,month,year)
print(day,month,year)