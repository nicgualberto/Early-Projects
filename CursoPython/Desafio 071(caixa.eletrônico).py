print('='*30)
print('\n BANCO DEV ')
print('-'*30)
valor_sacado = int(input('Digite o valor que deseja ser sacado: R$'))
total = valor_sacado
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0 
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO DEV.')