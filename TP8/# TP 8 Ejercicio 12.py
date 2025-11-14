# TP 8 Ejercicio 12
def main():
    # 1️⃣ Crear el diccionario de precios
    precios = {}

    print("Carga los productos de la librería. Escribí 'fin' para terminar.")
    while True:
        item = input("Producto: ")
        if item.lower() == "fin":
            break

        try:
            precio = float(input("Precio: "))
            precios[item] = precio
        except ValueError:
            print("Precio invalido. Intenta de nuevo.")

    if not precios:
        print("No se cargaron productos.")
        return

    
    for producto in precios:
        if "cuaderno" in producto.lower():
            precios[producto] *= 1.15

    
    print("\n=== LISTADO DE PRECIOS ===")
    for producto, precio in precios.items():
        print(f"{producto}: ${precio:.2f}")

    
    mas_caro = max(precios.items(), key=lambda x: x[1])
    print("\nEl item mas costoso es:")
    print(f" {mas_caro[0]} (${mas_caro[1]:.2f})")


if __name__ == "__main__":
    main()
