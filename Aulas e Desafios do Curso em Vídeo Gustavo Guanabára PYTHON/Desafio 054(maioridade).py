from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nascimento = int(input(f"Em que ano a {c}° nasceu: "))
    idade = atual - nascimento
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f"Ao todo tivemos \033[1;33m{totmaior}\033[m pessoas maior de idade!")
print(f"Ao todo tivemos \033[1;33m{totmenor}\033[m pessoas menor de idade!")