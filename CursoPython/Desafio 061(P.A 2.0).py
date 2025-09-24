print('\033[1;36mGERADOR DE P.A\033[m')
print('-=' * 10)
primeiro = int(input('Digite o primeiro valor da sua P.A: '))
razao = int(input('Digite a razao da sua P.A: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} > ', end='')
    termo += razao
    cont += 1
print('\033[1;32MFIM\033[M')