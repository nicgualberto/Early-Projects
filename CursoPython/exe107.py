from moeda import moedas

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é {moedas.metade(p)}')
print(f'O dobro de R${p} é {moedas.dobro(p)}')
print(f'Diminuindo 10% de R${p} fica {moedas.diminuir(p,10)}')
print(f'Aumentado 20% de R${p} fica {moedas.aumentar(p,20)}')