def mostrar_menu():
    while True:
        print("\n" + "=" * 50)
        print("SISTEMA DE ANALÍTICAS - TIENDA DE VIDEOJUEGOS")
        print("=" * 50)
        opciones = {
            "1": "Calcular facturación total",
            "2": "Mostrar stock disponible",
            "3": "Top 3 productos más vendidos",
            "4": "Salir"
        }
        for key, value in opciones.items():
            print(f"{key}. {value}")
        print("=" * 50)

        opcion = input("Selecciona una opción (1-4): ")
        if opcion == "1":
            calcular_facturacion()
        elif opcion == "2":
            mostrar_stock()
        elif opcion == "3":
            top_productos()
        elif opcion == "4":
            print("¡Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")
