numero = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite outro valor: ')), int(input('Último valor: ')))
numero_c = 9
quantidade = numero.count(numero_c)

print(f'A quantidade de vezes que o número {numero_c} foi contado: {quantidade} vezes')
if 3 in numero:
    print(f'O valor 3 apareceu na {numero.index(3)+1}° posição!')
else:
    print('O valor 3 não foi digitado!')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')
