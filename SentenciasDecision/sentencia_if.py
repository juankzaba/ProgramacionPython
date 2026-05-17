print(f'*** Sentencia If ***')

MAYOR_EDAD = 18
edad = int(input("Cuántos años tienes?: "))

if edad >= MAYOR_EDAD:
    print(f"Eres mayor de edad. Tienes {edad} años")
elif 13 <= edad < 18:
    print(f"Eres un adolescente. Tienes {edad} años")
else:
    print(f"Eres un niño. Tienes {edad} años")


