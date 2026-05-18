print('*** Aplicación Salud Fitness')

# Constantes
META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.04 # Valor aproximado, con kilocalorias

# Pedimos los valores al usuario
nombre_usuario = input("Cuál es tu nombre: ")
pasos_diarios = int(input("cuantos pasos has caminado hoy?: "))

# Verificamos si el usuario alcanzó la meta de pasos diarios
meta_alcanzada = pasos_diarios >=META_PASOS_DIARIOS
meta_alcanzada_txt = 'si' if meta_alcanzada else 'no'

# Calculamos las calorías quemadas
calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

# Mostramos la información
print(f'\nUsuario: {nombre_usuario}')
print(f'\nPasos dados hoy: {pasos_diarios}')
print(f'\nCalorías quemadas: {calorias_quemadas}')
print(f'\nMeta de pasos diaria alcanzada: {meta_alcanzada_txt}')
print(f'\nLa meta de paso diarios es: {META_PASOS_DIARIOS}')