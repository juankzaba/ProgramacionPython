'''Generador de Email

Crea un programa para generar un email a partir de los siguientes datos:

Nombre: Juan Carlos Zabala
Empresa: Cirion
Dominio: ciriontechnologies.com

Resultado Final:

*** Generador de Email ***
nombre usuario: Juan Carlos Zabala
nombre usuario normalizado: juan.carlos.zabala

Nombre empresa: CIRION
Extensión del dominio: ciriontechnologies.com
Dominio de email normalizado: @ciriontechnologies.com

email final generado: juan.carlos.zabala@ciriontechnologies.com


'''

# ***Generador Email***

print('*** Generador de Emails ***')
# Nombre completo del usuario
nombre_usuario = '  Juan Carlos Zabala  '
print(f'Nombre Usuario: {nombre_usuario}')

# Procesar o normalizar el nombre del usuario

# Limpiamos los espacios en blanco al inicio y al final
nombre_normalizado = nombre_usuario.strip()
print(f'Nombre Usuario: {nombre_normalizado}')

# Reemplazar los espacios en blanco por puntos
nombre_normalizado = nombre_normalizado.replace(' ','.')
print(f'Nombre Usuario: {nombre_normalizado}')

# Convertimos a minusculas
nombre_normalizado = nombre_normalizado.lower()
print(f'Nombre usuario: {nombre_normalizado}')

# Datos de la empresa
nombre_empresa = ' CIRION '
print(f'\nNombre empresa: {nombre_empresa}')

extension_dominio = '.Ciriontechnologies.com'
print(f'Extensión del dominio: {extension_dominio}')

# Quitamos los espacios en blanco y convertimos a mayusculas
nombre_empresa_normalizado = nombre_empresa.replace(' ', '').lower()
dominio_email_normalizado = f'@{nombre_empresa_normalizado}{extension_dominio}'
print(f'Dominio del email normalizado: {dominio_email_normalizado}')

# Creamos el email final
email = f'{nombre_normalizado}{dominio_email_normalizado}'
print(f'\nEmail final generado: {email}')