peso = float(input("Digite aqui seu peso: "))
altura = float(input("Digite aqui sua altura: "))

IMC = peso / (altura ** 2)

print("O seu IMC é {:.1f}".format(IMC))

if IMC < 18.5:
    print("Você está abaixo do peso.")
elif IMC >= 18.5 and IMC <= 24.9:
    print("Você está com o peso normal.")
elif IMC >= 25 and IMC <= 30:
    print("Você está com sobrepeso.")
else:
    print("Você se encontra em estado de obesidade.")