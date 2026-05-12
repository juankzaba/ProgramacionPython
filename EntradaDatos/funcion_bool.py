# Programa: función bool

# 1. Números (int y float)


print(bool(0)) # False (El vacío numérico)
print(bool(0.0)) # False
print(bool(42)) # True (Existe valor)

# 2. Texto (String)
# cadena vacia = Nada = False
print(bool("")) #False

# Cadena con espacio o texto = algo = True
print(bool(" ")) # True
print(bool("Hola")) # True

# 3. None (Ausencia total)

vacio = None
print(bool(vacio)) # False
print(bool(False)) # False
print(bool(True)) # True
