import numpy as np
arreglo = np.random.randint(1,100, size=10)

num = int(input("Ingrese un número a buscar en el arreglo "))

contador = 0
for idx in range(10):
    if arreglo[idx] == num:
        contador += 1 #contador = contador + 1         
if contador > 0:
    print(f"El número {num} SI esta en el arreglo")
    print("arreglo: ", arreglo)
else:
    print(f"El número {num} NO esta en el arreglo")
    print("arreglo: ", arreglo)