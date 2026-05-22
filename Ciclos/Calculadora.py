'''Crear una aplicación de calculadora con las opciones de:

Suma
Resta
Multiplicación
División

El programa debe mostrar un menú con cada opción, y debe solicitar los valores
 de operando 1 y operando 2 para realizar la operación seleccionada.'''

print('*** Calculadora en Python ***')

operando1 = operando2 = resultado = 0
salir = False
while not salir:
    print('''Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir
''')
    opcion = int(input("Escoje una opción: "))
    # Vamos a solicitar el valor del operando
    if 1 <= opcion <= 4:
        operando1 = float(input("Dame el valor 1: "))
        operando2 = float(input("Dame el valor 2: "))
    # Revisamos el tipo de operación a realizar
    if opcion == 1: # Suma
        resultado = operando1 + operando2
        print(f"El resultado de la suma es: {resultado:.2f}\n")
    elif opcion == 2: # Resta
        resultado = operando1 - operando2
        print(f"El resultado de la resta es: {resultado:.2f}\n")
    elif opcion == 3: # Multiplicación
        resultado = operando1 * operando2
        print(f"El resultado de la multiplicación es: {resultado:.2f}\n")
    elif opcion == 4: # División
        resultado = operando1 / operando2
        print(f"El resultado de la división es: {resultado:.2f}\n")
    elif opcion == 5:
        print(f"Saliendo del programa de calculadora. Hasta pronto!")
        salir = True
    else:
        print(f"Opción inválida, seleccione otra opción...\n")



