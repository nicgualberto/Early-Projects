def moeda(p):
    return f'R${p}'

def metade(p, show=False):
    if show:
        return f'R${p / 2}'
    return p / 2

def dobro(p, show=False):
    if show:
        return  f'R${p * 2}'
    return p * 2

def diminuir(p, tax, show=False):
    if show:
        percentual = tax / 100
        m = percentual * p
        return f'R${p - m}'
    percentual = tax / 100
    m = percentual * p
    return p - m

def aumentar(p, tax2, show=False):
    if show:
        percentual1 = tax2 / 100
        m1 = percentual1 * p
        return f'R${p + m1}'
    percentual1 = tax2 / 100
    m1 = percentual1 * p
    return p + m1

def resumo(p, tax1, tax2):
    
    print('RESUMO DO VALOR')
    print('-='*20)
    print(f'PREÇO ANALISADO: R${p}')
    print(f'DOBRO DO PREÇO:  R${dobro(p,show=True)}')
    print(f'METADE DO PREÇO: R${metade(p,show=True)}')
    print(f'{tax2}% de aumento:  R${aumentar(p, tax2, show=True)}')
    print(f'{tax1}% de redução:  R${diminuir(p,tax1,show=True)}')
    print('-='*20)
