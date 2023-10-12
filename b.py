califications = []


while True:
    while True:
        calification = input("Ingrese una calificacion \n")
        try:
            calification_decimal = float(calification)
            califications.append(float(calification))
            break
        except ValueError:
            print("Por favor ingrese una calificación numérica")

    cont = input("Desea continuar? y/n \n")

    if cont.lower() == "n":
        break


promedy = 0

for calification in califications:
    promedy += calification

print(f"El promedio total de las calificaciones ingresadas es: {
      (promedy / len(califications)): .2f}")
