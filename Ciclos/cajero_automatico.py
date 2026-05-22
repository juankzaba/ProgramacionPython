'''Crear la aplicación de cajero automático.

Las funciones principales de un cajero automático son: depositar, retirar y consultar el saldo.

El saldo puede tener un valor inicial
por ej. $1,000.00

Si haces un retiro se resta de tu saldo, y si haces un depósito se suma a tu saldo.

'''
print('*** Apicación de Cajero Automático ***')

saldo = 100000
salir = False
while not salir:
    print('''Menu:
        1. Consultar saldo
        2. Retirar 
        3. Depositar
        4. Salir  
        ''')
    opcion = int(input("Escoje una opción: "))
    if opcion == 1:
        print(f"Tu saldo actual es: ${saldo:.2f}\n")
    elif opcion == 2:
        retiro = float(input("Ingresa el monto a retirar: "))
        # Validación
        if retiro <= saldo:
            saldo -= retiro # Saldo = saldo -retiro
            print(f"Tu nuevo saldo es: ${saldo:.2f}\n")
        else:
            print(f"No cuentas con el saldo suficiente. Saldo actual es: ${saldo:.2f}\n")
    elif opcion == 3:
        deposito = float(input("Ingresa el monto a depositar: "))
        saldo += deposito  # Saldo = saldo + deposito
        print(f"Tu nuevo saldo es: ${saldo:.2f}\n")
    elif opcion == 4:
        print(f"Saliendo del cajero automático. Hasta pronto!")
        salir = True
    else:
        print(f"Opción inválida. Seleccione otra opción")
else:
    print(f"Terminando la aplicación de cajero Automático!")




