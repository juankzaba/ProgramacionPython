'''
Se pide crear un sistema que ofrezca descuentos dependiendo del monto de la compra, o si es miembro de la tienda

Se deben revisar las siguientes condiciones

1. Si ha comprado más de 1.00 y es miembro: Descuento del 10%
2.  Si solo es miembro de tienda: Descuento del 5%
3. Si no es miembro ni compro más de  1000: Descuento del 0%

*** Sistema de Descuentos ***

Cuál fé el monto de tu compra? 1500
Eres miembro de la tienda (si/no)? si

Felicidades, has obtenido un descuento del 10%
Monto de la compra: $1500.00
Monto del descuento: $150.00
Monto final de la compra con descuento: $1350.00
----------------------------------------------------------
Cuál fé el monto de tu compra? 800
Eres miembro de la tienda (si/no)? si

Felicidades, has obtenido un descuento del 5%
Monto de la compra: $800.00
Monto del descuento: $40.00
Monto final de la compra con descuento: $760.00

------------------------------------------------------------

Cuál fé el monto de tu compra? 700
Eres miembro de la tienda (si/no)? no

No obtuviste ningún tipo de descuento. Te invitamos a hacerte miembro de la tienda
Monto de la compra: $800.00
Monto del descuento: $40.00
Monto final de la compra con descuento: $700.00

'''

print('*** Sistema de Descuentos ***')

# Condiciones
MONTO_COMPRA_DESC = 1000

monto_compra = float(input("Cuál fué el monto de la compra: "))
eres_miembro = input("Eres miembro de la tienda (si/no)?: ")

descuento = 0
# Verificar cada caso con los datos proporcionados
if monto_compra >= MONTO_COMPRA_DESC and eres_miembro.strip().lower() == 'si':
    descuento = 0.1 # Descuento 10%
elif eres_miembro.strip().lower()== 'si':
    descuento = .05 # Descuento del 5%
elif monto_compra >= MONTO_COMPRA_DESC:
    descuento = .03 # Descuento del 3%
else:
    descuento = 0

# Hacemos los calculos respectivos para obtener el monto final
if descuento != 0:
    monto_descuento = monto_compra * descuento
    monto_final = monto_compra - monto_descuento
    print(f"\nFelicidades, has obtenido un descuento del {descuento * 100:.0f}%")
    print(f"Monto de la compra: ${monto_compra:.2f}")
    print(f"Monto del descuento: ${monto_compra:.2f}")
    print(f"Monto final de la compra con descuento: ${monto_final:.2f}")
else:
    print(f"\nNo obtuviste ningún descuento")
    print(f"Te invitamos hacerte miembro de la tienda")
    print(f"Monto final de la compra: ${monto_compra:.2f}")



