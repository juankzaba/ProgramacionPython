'''
 Sistema de descuentos VIP

 Una tienda de supermercado ofrece un descuento especial a clientes que compren 10 o más articulos por dia y ademas sean miembros de la tienda

 El sitema debe solicitar al cliente que indique cuantos articulos ha comprado en el dia y pregutarle si cuenta con la membresia de la tienda

 En caso de haber comrado 10 o más productos y ser miembro de la tienda entonces tendrá acceso al descuento VIP

'''

print(f"*** Sitema de descuentos VIP ***")
NUM_PRODUCTOS_DESCUENTOS = 10
cantidad_productos = int(input("Cuántos productos compraste hoy: "))
tiene_membresia = input("Tienes la membresía de la tienda (Si/No): ")

es_elegible_descuento = (cantidad_productos >= NUM_PRODUCTOS_DESCUENTOS
                         and tiene_membresia.strip().lower() == 'si') # Al dar enter antes de and cuándo está en una sola línea pycharm automaticamente abre paréntesis

print(f"Tienes acceso al descuento VIP?: {es_elegible_descuento}")
