print('*** Sistema de Envíos ***')

# Definimos las tarifas de envío por kilogramo
TARIFA_NACIOANAL = 10
TARIFA_INTERNACIONAL = 20

# Solicitamos los valores de destino y peso al usuario
destino = input("Ingresa el destino del paquete (nacional/internacional): ")
peso = float(input("Ingrese el peso del paquete (en kg): "))

# Cálculo del envío del paquete
costo_envio = None
destino = destino.strip().lower()
if destino == 'nacional':
    costo_envio = peso * TARIFA_NACIOANAL
elif destino == 'internacional':
    costo_envio = peso * TARIFA_INTERNACIONAL
else:
    print('Destino no válido. Ingrese el valor de nacional o internacional')

# Mostramos el costo del envio sólo si es un valor válido
if costo_envio is not None:
    print(f"El costo de envío del paquete es: ${costo_envio:.2f}")









