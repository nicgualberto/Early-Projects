import random
import time

tentativas = 1
userName = str(input('\033[1;37mNome de usuário: \033[m')).upper()
numero_secreto = random.randint(0, 10)
palpite = int(input('\033[1;35mDigite seu palpite: \033[m'))
while palpite != numero_secreto:
    tentativas += 1
    if palpite > numero_secreto:
        print(f'Ah, \033[1;36m{userName}\033[m, você errou. Chute um número menor!')
        time.sleep(0.5)
        palpite = int(input('\033[1;35mDigite seu palpite: \033[m'))
    else:
        print(f'Hmm, \033[1;37m{userName}\033[m, você não acertou. Tente um número maior!')
    
    time.sleep(1)
    palpite = int(input('\033[1;35mDigite seu palpite: \033[m'))
print(f'\033[1;32mVOCÊ ACERTOU! {userName} acertou em {tentativas} tentativas!\033[m')
        