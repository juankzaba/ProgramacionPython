'''

SISTEMA DE AUTENTICACIÓN

Crea un programa para validar el usairo y pass proporcionados por usuario.

Crea 2 constantes con los valores correcto y posteriormente compara que el usauri y pass proporcioanados por el usuario sean válidos
 Debe solicitar el usuario y el pass al usuario y si son iguales que los valores correcto almacenados en las constantes debe imprimir True, de lo contrario debe imprimir False

*** Sistema de Autenticación ***
Cual es tu usuario? admin
Cual es tu password? 123
Datos correcto? True

Cual es tu usuario? juan
Cual es tu password? 123
Datos correcto? False

'''
print('*** Sistema de Autenticación ***')

USUARIO_VALIDO = 'admin'
PASSWORD_VALIDO = '123'

usuario_ingresado = input("Cual es tu usuario?: ")
password_ingresado = input("Cual es tu password?: ")

son_datos_son_correctos = (usuario_ingresado.strip()== USUARIO_VALIDO
                           and password_ingresado.strip()== PASSWORD_VALIDO)

print(f"Los datos son correctos? {son_datos_son_correctos}")