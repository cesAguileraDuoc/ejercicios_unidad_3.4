import numpy as np

filas = 0
while filas < 3 or filas > 6:
  filas = int(input("Ingrese primer número entero entre 3 y 6 "))

columnas = 0
while columnas < 3 or columnas > 6:
  columnas = int(input("Ingrese segundo número entero entre 3 y 6 "))

matriz = np.random.rand(filas, columnas) #rand para numeros reales

print("matriz poblada ", matriz)

for fila in range(filas):
  print(f"suma fila {fila} = {matriz[fila,:].sum()}")

for col in range(columnas):
  print(f"promedio columna {col} = {matriz[:,col].mean()}")