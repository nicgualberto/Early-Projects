import random

print("Bem-vindo ao jogo de adivinhar o número")
numero_secreto = random.randint(1, 20)
tentativas = 0
acertou = False

while not acertou:
    palpite = int(input("Digite seu palpite (1-20): "))
    tentativas += 1
    
    if palpite == numero_secreto:
        print(f"Você acertou em {tentativas} tentativas, parabéns!")
        acertou =  True
    elif palpite < numero_secreto:
        print("Você errou, tente um número mais alto")
    else:
        print(f"Você errou, tente um número menor")