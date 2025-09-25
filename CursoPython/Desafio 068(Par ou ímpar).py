import random
import time

print('\n--- \033[1;31mPAR OU ÍMPAR\033[m ---')

total = True
escolha = ''
vitoria = 0
while True:
    escolha = str(input('Você quer ser ÍMPAR OU PAR [I/P]: ')).upper()
    if escolha == 'I':
        numero_computador1 = random.randint(1, 10)
        sua_vez = int(input('Digite aqui um número: '))
        resultado = numero_computador1 + sua_vez
        if resultado % 2 != 0:
            vitoria += 1
            print('...')
            time.sleep(2)
            print(f'Você jogou {sua_vez} e o computador jogou {numero_computador1}')
            print(f'Você é top, ganhou do computador! {resultado} é ÍMPAR!')
        else:
            print(f'Você jogou {sua_vez} e o computador jogou {numero_computador1}')
            print(f'Você perdeu! {resultado} é PAR!')
            print('----' * 10)
            print(f'Você ganhou {vitoria} vezes do computador!')
            break
    elif escolha == 'P':
        numero_computador1 = random.randint(1, 10)
        sua_vez = int(input('Digite um número: '))
        resultado = numero_computador1 + sua_vez
        if resultado % 2 == 0:
            vitoria += 1
            print('...')
            time.sleep(2)
            print(f'Você jogou {sua_vez} e o computador jogou {numero_computador1}')
            print(f'Você é top, ganhou do computador! {resultado} é PAR!')
        else:
            print(f'Você jogou {sua_vez} e o computador jogou {numero_computador1}')
            print(f'Você perdeu! {resultado} é ÍMPAR!')
            print('----' * 10)
            print(f'Você ganhou {vitoria} vezes do computador!')
            break

            
            
    