import numpy as np
import time
print("CALCULE A DETERMINANTE")
time.sleep(1)
n = float(input("Digite um valor: "))
n2 = float(input("Digite o segundo valor: "))
n3 = float(input("Terceiro valor: "))
n4 = float(input("Quarto valor: "))
n5 = float(input("Quinto valor: "))
n6 = float(input("Sexto valor: "))

time.sleep(1)
matriz_exe = np.array([[n, n2, 1],
                       [n3, n4, 1],
                       [n5, n6, 1]])

determinante = np.linalg.det(matriz_exe)
time.sleep(1)
print(f"O determinante da matriz é: {determinante :.2f}")