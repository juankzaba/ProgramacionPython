print('*** Bienvenidos a la casa de espejos')

edad = int(input("Cual es tu edad: "))
tienes_miedo_oscuridad = input("Le tienes miedo a la oscuridad (si/no)?: ")
tienes_miedo_oscuridad = tienes_miedo_oscuridad.strip().lower()=='si'

if not tienes_miedo_oscuridad and edad >=10:
    print(f"Puedes estrar a la casa de los espejos")
else:
    print(f"Lo siento, la casa de los espejos podría darte miedo")




