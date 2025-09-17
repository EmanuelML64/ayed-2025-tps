# TP 2 Ejercicio 12
# Algoritmos y estructura de datos
socios = []
numero = int(input("Ingrese el numero de socio, 5 digitos: "))
while numero != 0:
    socios.append(numero)

socio = []
cantidad = []

for soc in socios:
    if soc not in socio:
        socio.append(soc)

for soc in socio:
    cantidad.append(socios.count(soc))

for soc,cant in zip(socio,cantidad):
    print(f"El socio {soc} tuvo {cant} ingresos al club")

print("Ingresos: ")
print(cantidad)

baja = int(input("Ingrese el numero de socio a eliminar: "))
if baja in socios:
    for i in range(socios.count(baja)):
        socios.remove(baja)
else:
    print("Codigo de socio no valido")

print("La nueva lista es: ")
print(socios)

