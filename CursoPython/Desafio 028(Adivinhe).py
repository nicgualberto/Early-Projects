import random

userName = str(input("Digite aqui seu nome de usuário: "))
print(f"Olá, {userName}!")

numero_secreto = random.randint(0, 5)
palpite = int(input("Tente adivinhar o número: "))
if palpite == numero_secreto:
    print(f"Você é muito bom nisso, o número que eu pensei foi o {numero_secreto}")
else:
    print(f"Tente novamente, {userName}! Você perdeu.")
print("--FIM--")