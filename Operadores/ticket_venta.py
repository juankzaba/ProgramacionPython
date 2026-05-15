'''GENERACIÓN TICKET VENTA
sUPONGAMOS QUE COMPRAMOS VARIOS ARTICULOS EN EL SUPERMERCADO Y QUEREMOS OBTENER EL TICKET DE VENTA TOTAL
incluyendo impuestos.

EL sistema solicitará el precio de cada producto a compar y el usuario deberá indicar su precio(valor de tipo con un punto decimal)

El sistema debe realizar la suma de cada producto, calucular el impuesto y finalmente imprimir el total de la compra

'''
print('***Gemeración ticket de venta ***')

precio_leche = float(input("Precio Leche: "))
precio_pan = float(input("Precio Pan: "))
precio_lechuga = float(input("Precio Lechuga: "))
precio_platanos = float(input("Precio Plátano: "))
descuento_porcentaje = int(input("Aplicar algún descuento (%): "))

# Calculo del subtotal (sin impuetos)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

# Aplicar el descuento
descuento = subtotal *(descuento_porcentaje/100)

# Subtotal con descuento
subtotal_con_descuento = subtotal - descuento

# Calculo con impuestos (16%)
impuesto = subtotal_con_descuento * 0.16

# Calculo total de la compra (con impuestos)
costo_total_compra = subtotal_con_descuento + impuesto
print(f'''
subtotal: ${subtotal:.2f}
Descuento: ${descuento} ({descuento_porcentaje}%)
Subtotal con descuento: ${subtotal_con_descuento}
Impuesto (16%): ${impuesto:.2f}
Costo total de la compra: ${costo_total_compra:.2f}
''')