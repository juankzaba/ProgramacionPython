print('*** Sistema de Autenticación ***')

USUARIO_VALIDO = 'admin'
PASSWORD_VALIDO = '123'

usuario = input("Ingresa tu usuario: ")
password = input("Ingresa tu password: ")

if usuario == USUARIO_VALIDO and password == PASSWORD_VALIDO:
    print(f"Bienvenido al sistema!")
elif usuario == USUARIO_VALIDO:
    print(f"Password incorrecto, por favor corregirlo")
elif password == PASSWORD_VALIDO:
    print(f"Usuario incorrecto, por favor corregirlo")
else:
    print(f"Credenciales inválidas, intente de nuevo")
