from random import randint
numero = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números sorteados foram {numero}')
max_value = max(numero)
min_value = min(numero)
print(f'O maior valor foi: {max_value}')
print(f'O menor valor foi: {min_value}')