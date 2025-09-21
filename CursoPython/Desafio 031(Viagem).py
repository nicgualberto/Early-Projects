userName = str(input("Digite o nome de usuário: "))
viagem = float(input(f"{userName}, digite aqui a distância da sua viagem (Em Km): "))

if viagem <= 200:
    passagem = viagem * 0.50
    print(f"O valor da passagem é de: R$ {passagem :.2f}")
else:
    passagem2 = viagem * 0.45
    print(f"O valor da passagem é de: R$ {passagem2 :.2f}")
print("==FIM==")