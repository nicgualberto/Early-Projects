total = 0
totalmil = 0
menor = 0
cont = 0
while True:
    produto = str(input('Digite o nome do produto: ')).upper()
    preco = float(input('O valor do produto: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totalmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'YN':
        resp  = str(input('Você deseja continuar[Y/N]: ')).upper()
    if resp == 'N':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total de compra foi R${total:.2f}')
print(f'Temos {totalmil} produtos custando mais de R$1000,00')
print(f'O produto mais barato custa R${menor:.2f}')