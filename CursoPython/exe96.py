'''função que calcule a área de um determinado espaço'''

def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}m².')


print('CONTROLE DE TERRENOS')
print('-'*20)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)