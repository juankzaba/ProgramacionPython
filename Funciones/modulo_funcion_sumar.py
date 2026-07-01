# Definimos la función
def sumar(a,b):
    resultado_suma = a+b
    return resultado_suma

# Prueba de la función sumar
if __name__ == '__main__': # Para que no se ejecute también en la función ppal sumar_2
    print(f"Prueba función sumar desde el módulo:{sumar(15,30)}")