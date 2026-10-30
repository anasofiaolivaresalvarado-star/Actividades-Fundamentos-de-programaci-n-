# ============================================================
# Sistema de registro y calculo de ventas para una papeleria.
# Proyecto basado en Papelerias Colibri.
# ============================================================

total_dia = 0.0
numero_ventas = 0
continuar_sistema = True

while continuar_sistema:
    print("\n===== SISTEMA DE VENTAS =====")
    print("1. Registrar venta")
    print("2. Consultar resumen")
    print("3. Salir")

    try:
        opcion = int(input("Seleccione una opcion: "))
    except ValueError:
        print("Error: debe ingresar un numero.")
        continue

    if opcion == 1:
        subtotal = 0.0
        hay_productos = False

        print("\n===== REGISTRO DE VENTA =====")
        print("Escriba FIN como nombre para terminar la captura.")

        while True:
            nombre_producto = input(
                "Nombre del producto: "
            ).strip()

            if nombre_producto.upper() == "FIN":
                break

            if nombre_producto == "":
                print("El nombre no puede estar vacio.")
                continue


            try:
                precio_unitario = float(
                    input("Precio unitario: $")
                )

                if precio_unitario < 0:
                    print("El precio no puede ser negativo.")
                    continue

                cantidad = int(
                    input("Cantidad de unidades: ")
                )

                if cantidad <= 0:
                    print("La cantidad debe ser mayor que cero.")
                    continue

            except ValueError:
                print(
                    "Error: ingrese un precio numerico "
                    "y una cantidad entera."
                )
                continue

            importe_producto = precio_unitario * cantidad
            subtotal += importe_producto
            hay_productos = True

            print(f"Producto: {nombre_producto}")
            print(f"Importe: ${importe_producto:.2f}")

        if hay_productos:
            total_venta = subtotal
            total_dia += total_venta
            numero_ventas += 1

            print("\n===== RESUMEN DE LA VENTA =====")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Total de la venta: ${total_venta:.2f}")
            print("Venta registrada correctamente.")
        else:
            print("No se registro ninguna venta.")

    elif opcion == 2:
        print("\n===== RESUMEN DE VENTAS =====")
        print(f"Ventas registradas: {numero_ventas}")
        print(f"Importe acumulado: ${total_dia:.2f}")

    elif opcion == 3:
        continuar_sistema = False

    else:
        print("Opcion no valida. Intente nuevamente.")

print("\n===== CIERRE DEL SISTEMA =====")
print(f"Ventas registradas: {numero_ventas}")
print(f"Importe acumulado: ${total_dia:.2f}")
print("Programa finalizado.")
