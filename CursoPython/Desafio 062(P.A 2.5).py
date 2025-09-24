import time

print('\033[1;36mGERADOR DE P.A V2\033[m')
print('-=' * 10)
primeiro = int(input('Digite o primeiro valor da sua P.A: '))
razao = int(input('Digite a razao da sua P.A: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} > ', end='')
        termo += razao
        cont += 1
    print('\033[1;32mPAUSE\033[m')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos contados!')
print('...')
time.sleep(2)
print('FIM!')