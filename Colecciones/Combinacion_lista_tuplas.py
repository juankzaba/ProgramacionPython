print('*** Combinación de Listas y Tuplas')

# Definir una lista que almacena tuplas de productos
productos = [
    ('POO1','Camiseta', 20.00),
    ('POO2','Jeans', 30.00),
    ('POO3','Sudadera',40.00)
]

# Imprimir la información de cada producto
# Y además calculamos el precio total
precio_total = 0

print('Información de los productos: ')
for producto in productos:
    # print(producto)
    id, descripcion, precio = producto # Unpacking
    print(f"Producto: id = {id}, descripción = {descripcion}, precio = {precio}")
    precio_total += precio # Producto [2]
print(f"Precio total de los productos: ${precio_total}")











