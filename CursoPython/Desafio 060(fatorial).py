from math import factorial
import time

numero = int(input('Digite um número para calcular seu fatorial: '))
contador = numero
f = 1
print('...')
time.sleep(2)
print(f'Calculando {numero}! = ', end='')
while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    f *= contador
    contador -= 1
print(f'{f}')
#print(f'O fatorial de {numero} é {f}.')

