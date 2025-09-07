nome = str(input("Digite aqui seu nome: "))
numero = int(input("Digite um valor: "))
for i in range(1,21):
        resultado = numero * i
        print(f"{numero} * {i} é igual a {resultado}")
while True:
    frase = input("Você deseja calcular outro valor? (S/N)")
    if frase.upper() == "N":
        print(f"Obrigado, {nome}. Até mais!")
        break
    else:
        outro_valor = int(input("Digite aqui um valor: "))
    for a in range(1,21):
        igualdade = outro_valor * a
        print(f"Tabuada do {outro_valor}: ")
        print(f"{outro_valor} * {a} é igual a {igualdade}")