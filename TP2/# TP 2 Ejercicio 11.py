# TP 2 Ejercicio 11
# Algoritmos y estructura de datos
pacientesconturno = []
pacientesconurgencias = []
afiliado = int(input("Ingrese sus cuatro digitos de numero de afiliado: "))
while afiliado != -1:
    nivel = int(input("Ingrese 0 para urgencias o 1 si viene con turno: "))
    if nivel == 0:
        pacientesconurgencias.append(afiliado)
    else:
        pacientesconturno.append(afiliado)
    afiliado = int(input("Ingrese su numero de afiliado: "))
print("Con turno: ",pacientesconturno)
print("Con urgencias: ",pacientesconurgencias)

encontradoconturno = 0
encontradoconurgencias = 0
busqueda = int(input("Ingrese un numero de afiliado a buscar: "))
while busqueda != -1:
    for paciente in pacientesconturno:
        if busqueda == paciente:
            encontradoconturno += 1
    for patient in pacientesconurgencias:
        if busqueda == patient:
            encontradoconurgencias += 1
print("Con turno:", encontradoconturno)
print("Con urgencias: ",encontradoconurgencias)
