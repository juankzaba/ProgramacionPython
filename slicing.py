#Programa: Aplicar el concepto de slicing

texto = 'PROGRAMACIÓN'

# 1. Basico [ínicio:fin]
print(texto[0:4]) # 'PROG' (El indice 4 no se incluye)

# 2. Atajo desde el inicio [:fin]
print(texto[:4]) # 'PROG' (Asume inicio 0)

# 3. Atajo hasta el final [inicio:]
print(texto[8:]) # 'CION' (Hasta el último caracter)

# 4. Indices Negativos
print(texto[-4:]) # 'CION' (Los ultimos 4)

# 5. Pasos [::pasos] (Invertir cadena)
print(texto[::-1]) # 'NOICAMARGORP'
print(texto[::1]) # 'NOICAMARGORP'
print(texto[::-2]) # 'NIAAGR'
print(texto[::2]) # 'PORMCÓ'
