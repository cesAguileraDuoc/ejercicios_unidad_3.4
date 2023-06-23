def calcular_total_pagar(expressos, capuchicos, lattes, moccas):
    sub_total = 0
    descuento = 0

    sub_total = sub_total + (expressos*1500)
    sub_total = sub_total + (capuchicos*1800)
    sub_total = sub_total + (lattes*1600)
    sub_total = sub_total + (moccas*1700)

    if sub_total > 3000:
        descuento = round((sub_total * 10)/100)

    total_pagar = sub_total - descuento
    return total_pagar, sub_total, descuento

menu = True

cont_expresso = 0
cont_capuchico = 0
cont_latte = 0
cont_mocca = 0

while menu:
    print(f"1. Espresso $1.500 {cont_expresso}")
    print(f"2. Capuchino $1.800 {cont_capuchico}")
    print(f"3. Latte $1.600 {cont_latte}")
    print(f"4. Mocca $1.700 {cont_mocca}")
    print("5. Pagar")

    try:
        opcion = int(input("Escoja una opción "))
    except:
        print("Valor no valido")
        continue

    if opcion < 1 or opcion > 5:
        print("Opción no existente")
        continue

    if opcion == 1:
        cont_expresso += 1

    if opcion == 2:
        cont_capuchico += 1

    if opcion == 3:
        cont_latte += 1

    if opcion == 4:
        cont_mocca += 1

    if opcion == 5:
        total_pagar, sub_total, descuento = calcular_total_pagar(cont_expresso, cont_capuchico, cont_latte, cont_mocca)
        print("--- PAGAR ---")
        print(f"Subtotal: {sub_total}")
        print(f"Descuento: {descuento}")
        print(f"Total Pagar: {total_pagar}\n")
        menu = False