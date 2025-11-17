import random
import time


def sorteia(numeros):
    print(f'Sorteando 5 valores da lista...')
    for num in range(0, 5):
        n = random.randint(1, 10)
        numeros.append(n)
        print(f'{n} ', end='', flush=True)
        time.sleep(0.5)
    print('PRONTO')


def somePar(numeros):
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos números pares resultou em {soma}')


numeros = []
sorteia(numeros)
somePar(numeros)
