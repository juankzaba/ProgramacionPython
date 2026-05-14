print('*** Sistema Generador de Email ***')
nombre = input("Cuál es tu nombre: ")
apellidos = input("Cuál es tu apelllido: ")
empresa = input("Nombre de tu empresa: ")
extension_dominio = input("Extensión del dominio de tu empresa: ")

# Normalizamos los valores recibidos
nombre = nombre.strip().lower().replace(' ','.')
apellidos = apellidos.strip().lower().replace(' ','.')
empresa = empresa.strip().lower().replace(' ','.')
extension_dominio = extension_dominio.strip().lower().replace(' ','.')

# Generar email
email = f'{nombre}.{apellidos}@{empresa}{extension_dominio}'

print(f'''
Tu nuevo email gnerado por el sistema es:
    {email}
    Felicidades!
''')