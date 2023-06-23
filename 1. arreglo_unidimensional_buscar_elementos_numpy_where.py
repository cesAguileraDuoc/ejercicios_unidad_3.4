import numpy as np
arreglo = np.random.randint(1,100, size=10)

num = int(input("Ingrese un número a buscar en el arreglo "))

result = np.where(arreglo==num)
if len(result[0]) > 0:
    print(f"El número {num} SI esta en el arreglo")
    print("arreglo: ", arreglo)
else:
    print(f"El número {num} NO esta en el arreglo")
    print("arreglo: ", arreglo)