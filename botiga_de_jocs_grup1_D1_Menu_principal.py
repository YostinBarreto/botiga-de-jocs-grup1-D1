def calcular_facturacio():
    print("Calculando la facturación...")  
    

def calcular_estoc_disponible():
    print("Calculando el estoc disponible...")  
   

def resum_products():
    print("Resumen de los productos...")  
    

def menu_principal():
    print("1. Calcular facturación")
    print("2. Calcular estoc disponible")
    print("3. Resumen de productes")
    print("4. Salir")

    opcio = input("Selecciona una opción: ")

    if opcio == "1":
        calcular_facturacio()
    elif opcio == "2":
        calcular_estoc_disponible()
    elif opcio == "3":
        resum_products()
    elif opcio == "4":
        print("Saliendo del programa...")
    else:
        print("Opción no vàlida!")

menu_principal()
