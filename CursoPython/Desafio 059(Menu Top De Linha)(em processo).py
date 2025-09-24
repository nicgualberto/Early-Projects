import random
import time

user = str(input('\033[1;37mCrie seu usuário: \033[m')).upper()
num1 = int(input("Digite aqui o primeiro valor: "))
num2 = int(input("Digite aqui o segundo valor: "))
escolha = 0

while escolha != 5:
    print("\n=== \033[1;33mMENU TOP DE LINHA\033[m ===")
    print("""\033[1;31m    [1] SOMAR\033[m
    \033[1;32m[2] MULTIPLICAR\033[m
    \033[1;33m[3] NÚMERO ALEATÓRIO\033[m
    \033[1;34m[4] NOVOS NÚMEROS\033[m
    \033[1;36m[5] SAIR DO PROGRAMA\033[m
           """)
    escolha = int(input(f'\033[1;37m{user}\033[m, escolha uma das opções \033[1;33m[1-5]\033[m: '))
    if escolha == 1:
        soma = num1 + num2
        print(f"A soma entre os dois valores digitados foi: \033[1;31m{soma}\033[m")
    elif escolha == 2:
        multiplicacao = num1 * num2
        print(f'O resultado dessa multiplicação foi: \033[1;32m{multiplicacao}\033[m')
    elif escolha == 3:
        numero_secreto = random.randint(1, 1000)
        print('O número aleatório gerado para você foi...')
        time.sleep(2)
        print(f'\033[1;33m{numero_secreto}\033[m')
    elif escolha == 4:
        num1 = int(input('Digite um novo valor: '))
        num2 = int(input('Segundo novo valor: '))
        print(f'Seus novos valores: \033[34{num1}, {num2}\033[m')
    elif not escolha in [1,2,3,4,5]: 
        print('\033[1;31mDigite um valor correspondente com as escolhas do programa, por favor!\033[m')
print('...')
time.sleep(2)
print(f'Até mais, \033[1;32m{user}\033[m! \033[1;37mTenha uma semana abençoada!\033[m')

