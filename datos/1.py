# Menú Principal
print("Bienvenido a Comida al paso")
print("1. Registrar Venta")
print("2. Consultar Ventas")
print("3. Salir")

opcion = int(input("Ingrese Opción: "))

while opcion != 3:
    if opcion == 1:
        # Registrar Venta
        print("11. Hamburguesa")
        print("12. Completo")
        print("13. Papas Fritas")
        print("14. Salir")

        venta = input("Ingrese Opción: ")
        if venta == "11":
            # Hamburguesa
            base_price = 1500
            ingredientes = []
            precios = {
                "palta": 800,
                "tomate": 700,
                "cebolla": 600,
                "mayo": 500,
                "mostaza": 400
            }

            for ingrediente in ["palta", "tomate", "cebolla", "mayo", "mostaza"]:
                respuesta = input(f"Desea {ingrediente} sí o no: ")
                if respuesta.lower() == "si":
                    ingredientes.append(ingrediente)
                    base_price += precios[ingrediente]

            print(f"Su venta es de: {base_price}")

        elif venta == "12":
            # Completo
            base_price = 1200
            ingredientes = []
            precios = {
                "palta": 700,
                "tomate": 600,
                "chucrut": 500,
                "mayo": 500,
                "mostaza": 400
            }

            for ingrediente in ["palta", "tomate", "chucrut", "mayo", "mostaza"]:
                respuesta = input(f"Desea {ingrediente} sí o no: ")
                if respuesta.lower() == "si":
                    ingredientes.append(ingrediente)
                    base_price += precios[ingrediente]

            print(f"Su venta es de: {base_price}")

        elif venta == "13":
            # Papas Fritas
            tipo_papa = input("Desea papa familiar sí o no: ")
            if tipo_papa.lower() == "si":
                base_price = 5000
            else:
                base_price = 0

            print(f"Su venta es de: {base_price}")

        print("\n")

    elif opcion == 2:
        # Consultar Ventas
        total_ventas = int(input("El total de ventas hasta el momento es de: "))
        print(f"El total de ventas hasta el momento es de: {total_ventas}\n")

    print("1. Registrar Venta")
    print("2. Consultar Ventas")
    print("3. Salir")

    opcion = int(input("Ingrese Opción: "))

print("Adiós!")