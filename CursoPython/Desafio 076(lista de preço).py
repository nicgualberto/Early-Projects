materiais = ('Lápis', 1.50,
            'Borracha', 2,
            'Estojo', 10.50,
            'Mochila', 100,
            'Apontador', 5,
            'Farda', 90,
            'Caderno', 21.50,
            'Marca-Texto', 12.50)
print('-' * 40)
print(f'{"LISTA DE MATERIAL ESCOLAR":^40}')
print('-'* 40)
for item in range(0, len(materiais)):
    if item % 2 == 0:
        print(f'{materiais[item]:.<40}', end='')
    else:
        print(f'R${materiais[item]:>7.2f}')