def area_circulo(radio):
    return radio**2

def perimetro_cuadrado(lado):
    return lado*4

opcion = 0
menu = True
while menu:
    print("1: Área de un Circulo")
    print("2: Perímetro de un Cuadrado")
    print("3: Salir")

    try:
        opcion = int(input("Escoja una opción "))
    except:
        print("Valor no valido")
        continue

    if opcion < 1 or opcion > 3:
        print("Opción no existente")
        continue

    if opcion == 1:
        radio = int(input("Ingrese el radio del circulo "))
        area = area_circulo(radio)
        print(f"El área del circulo cuyo radio es {radio} es {area}\n")

    if opcion == 2:
        lado = int(input("Ingrese el lado del cuadrado "))
        perimetro = perimetro_cuadrado(lado)
        print(f"El perimetro del cuadrado cuyo lado es {lado} es {perimetro}\n")

    if opcion == 3:
        print("Adios")
        menu = False