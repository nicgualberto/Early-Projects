import time
print("P.A")
a1 = int(input("Digite o primeiro termo da P.A: "))

r = int(input("Digite a razão: "))

contador = 1
termo_atual = a1

time.sleep(1)

print("\n--- OS 10 PRIMEIROS TERMOS DA P.A ---")

while contador <= 10:
    print(f"{contador}° termo: {termo_atual}")
    termo_atual = termo_atual + r
    contador = contador + 1