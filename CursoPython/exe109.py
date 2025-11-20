from moeda import moedas

p = float(input('Digite o preço: R$'))
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p,show=True)}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p, True)}')
print(f'Diminuindo 10% de {moedas.moeda(p)}, resulta {moedas.diminuir(p,10, False)}')
print(f'Aumentado 20% de {moedas.moeda(p)}, resulta {moedas.aumentar(p,20, True)}')