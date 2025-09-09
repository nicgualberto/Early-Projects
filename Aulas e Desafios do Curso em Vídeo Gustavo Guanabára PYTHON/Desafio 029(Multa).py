motorista = str(input("Qual seu nome? "))
velocidade = float(input(f"Digite aqui a velocidade do seu veículo, {motorista} (Em Km/h): "))

if velocidade > 80 :
    multa = (velocidade - 80) * 7.00
    print(f"O seu veículo foi mutado no valor de: R$ {multa :.2f} ")
else:
    print(f"Pode passar, {motorista}! Você está dentro das normas.")