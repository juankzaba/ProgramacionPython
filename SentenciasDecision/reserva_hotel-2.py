print('*** Sistema de Reserva de Hote')

# Variables de hotel
tarifa_diaria_sin_vista_mar = 150.50
tarifa_diaria_con_vista_mar = 190.50

# Pedimos información del usuario
nombre_cliente = input("Nombre del cliente: ")
dias_estadia = int(input("Días de estadia: "))
vista_al_mar_txt = input("Con vista al mar: ")
vista_al_mar = vista_al_mar_txt.strip().lower()=='si'

# Calculo del costo total de la instancia
if vista_al_mar:
    costo_total = dias_estadia * tarifa_diaria_con_vista_mar
else:
    costo_total = dias_estadia * tarifa_diaria_sin_vista_mar

# Mostrar los detalles de la reserva
print('\n---------Detalles de la reservación------------')
print(f"Cliente: {nombre_cliente}")
print(f"Días de estadía: {dias_estadia}")
print(f"Costo total: ${costo_total:.2f}")
print(f"Habitación con vista al mar: {'si' if vista_al_mar else 'no'}")