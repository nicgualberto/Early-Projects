nome = str(input("Qual é seu nome? "))
if nome == "Nic":
    print("Que nome lindo você tem!")
else:
    print("Seu nome é tão normal.")
print(f"Bom dia, {nome}!")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
print("Sua média foi {:.1f}".format(media))
if media >= 9.0:
    print("Sua média foi muito boa! PARABÉNS!")
elif media <= 8 or media >= 6:
    print("Estude mais!")
else:
    print("Na próxima você consegue! ")