'''Crear una aplicación de calculadora con las opciones de:

Suma
Resta
Multiplicación
División

El programa debe mostrar un menú con cada opción, y debe solicitar los
valores de operando 1 y operando 2 para realizar la operación seleccionada.'''

print(' *** Creación y validación de un password **')

password = input("Ingresa un password (debe tener al menos 6 caracteres): ")

# Validar password
while len(password)< 6:
    print(f"El password no cumple con los requisitos. Debe tener al menos 6 caracteres")
    password = input("Ingresa un nuevo valor de password: ")
else:
    print(f"El valor de password es válido")