from moeda import moedas

p = float(input('Digite o preço: R$'))
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p)}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p)}')
print(f'Diminuindo 10% de {moedas.moeda(p)}, resulta {moedas.diminuir(p,10)}')
print(f'Aumentado 20% de {moedas.moeda(p)}, resulta {moedas.aumentar(p,20)}')