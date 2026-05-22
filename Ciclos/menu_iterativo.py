print('*** Sistema de administración de Cuentas ***')

salir = False
while not salir:
    print('''Menu:
    1. Crear cuenta
    2. Eliminar cuenta
    3. Salir  
    ''')
    opcion = int(input("Escoje una opción: "))
    if opcion == 1:
        print('Creando tu cuenta...\n')
    elif opcion == 2:
        print('Eliminando tu cuenta...\n')
    elif opcion == 3:
        print('Saliendo del sistema. Hasta pronto\n')
        salir = True
    else:
        print('Opción inválida, proporciona otra opción\n')
else:
    print(f"Terminando el sistema de Administración de cuentas")