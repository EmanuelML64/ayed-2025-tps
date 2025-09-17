# TP 1 Ejercicio 3
# Algoritmos y Estructuras de datos
def tarifasubte(viajes: int)-> int:
    tarifa = 1000
    masde20 = 800
    masde30 = 700
    masde40 = 600
    if viajes <= 20:
        costo = viajes*tarifa
    elif viajes > 20 and viajes <= 30:
        costo = (viajes - 20) * masde20 + 20 * tarifa
    elif viajes > 30 and viajes <= 40:
        costo = (viajes - 30) * masde30 + 10 * masde20 + 20 * tarifa
    else:
        costo = (viajes - 40) * masde40 + 10 * masde30 + 10 * masde20 + 20 * tarifa
    return costo
cantidad = int(input("Ingrese la cantidad de viajes realizados: "))
total = tarifasubte(cantidad)
print("Su costo es ", total, "$")
