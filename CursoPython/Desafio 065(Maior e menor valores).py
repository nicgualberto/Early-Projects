print('\n--- NÚMEROS ---')
escolha = ''
numeros = []
while escolha != 'N':
    numeros.append(int(input('Digite aqui um valor: ')))
    escolha = str(input('Você deseja continuar digitando valores [Y/N]: ')).upper()
    total = len(numeros)
    maior = max(numeros)
    menor = min(numeros)
    media = sum(numeros) / total
print(f'''
A média entre os valores digitados foi: {media}
O maior número da lista foi o valor {maior}
E o menor número da lista foi o valor {menor}
''')
    