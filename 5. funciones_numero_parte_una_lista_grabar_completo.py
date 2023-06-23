productos = []

def nro_parte_valido(nro):
    if len(nro) < 10:
        return False

    try:
        seis_primeros_digitos = int(nro[0:6])
    except:
        #Si no son número responde false
        return False
    
    #Si el septimo dígito no es guión responde false
    if nro[6] != "-":
        return False
    
    #Si lo anterior funciona bien responde true
    return True

def nombre_producto_valido(nombre):
    if len(nombre) >= 6:
        return True
    return False

def precio_producto_valido(precio):
    if precio > 0:
        return True
    return False

def guardar(nro_parte, nombre_producto, descripcion_producto, precio_producto):
    my_producto = [nro_parte, nombre_producto, descripcion_producto, precio_producto]
    productos.append(my_producto)

def buscar_producto(valor):
    for i in range(len(productos)):
        if productos[i][0] == valor:
            return i
    #Retorna una poción no valida cuando no lo encuentra
    return -1

def obtener_precio(index):
    return productos[index][3]

def imprimir_ficha(index):
    print(f"Nombre del Producto: {productos[index][1]}")
    print(f"Número de Parte: {productos[index][0]}")
    print(f"Descripción del Producto: {productos[index][2]}")
    print(f"Valor del Producto: {productos[index][3]}")

menu = True
while menu:
    print("1: Grabar")
    print("2: Buscar")
    print("3: Imprimir")
    print("4: Salir")

    try:
        opcion = int(input("Escoja una opción "))
    except:
        print("Valor no valido")
        continue

    if opcion < 1 or opcion > 4:
        print("Opción no existente")
        continue

    if opcion == 1:
        nro_parte = ""
        while nro_parte_valido(nro_parte) == False:
            nro_parte = input("Ingrese número de parte ")

        nombre_producto = ""
        while nombre_producto_valido(nombre_producto) == False:
            nombre_producto = input("Ingrese nombre del producto ")

        # Para la funcionalidad de imprimir
        descripcion_producto = input("Ingrese descripcion del producto ")

        precio_producto = 0
        while precio_producto_valido(precio_producto) == False:
            precio_producto = int(input("Ingrese precio del producto "))

        # Después que todos los campos estén validados los guardo
        guardar(nro_parte, nombre_producto, descripcion_producto, precio_producto)

    if opcion == 2:
        nro_parte_buscar = input("Ingrese número de parte a buscar ")
        index_producto = buscar_producto(nro_parte_buscar)

        if index_producto > -1:
            precio_producto_buscar = obtener_precio(index_producto)

            if precio_producto_buscar >= 500:
                imprimir_ficha(index_producto)
            else:
                print("Producto sin Stock")
        else:
            print(f"Producto {nro_parte_buscar} no registrado")

    if opcion == 3:
        print("REPORTE")
        print("-----------------")
        for i in range(len(productos)):
            imprimir_ficha(i)
            print("-----------------\n")

    if opcion == 4:
        print("Usted ha salido del programa!")
        print("Muchas gracias!")
        print("Autor: César Aguilera Sepúlveda")
        print("Versión: 1.0\n")
        menu = False