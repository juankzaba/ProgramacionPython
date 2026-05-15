# Revisar si una variable se encuentr dentro de rango 1 y 10


dato = int(input("Proporciona un dato entero: "))

# Revisamos si está dentro de Rango
esta_dentro_de_rango = 1 <= dato <= 10
print(f"Variable está dentro de rango (entre 1 y 10)?: {esta_dentro_de_rango}")

# Revisamos lo lógica inversa, si el dato está fuera de esta_dentro_de_rango
esta_fuera_rango = not(1 <= dato <= 10)
print(f"Variable está fuera de rango (entre 1 y 10)?: {esta_fuera_rango}")
