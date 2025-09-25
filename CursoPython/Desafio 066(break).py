numeros = 0
soma = 0
while True:
    numeros = int(input('Digite um valor[999 para parar]: '))
    if numeros == 999:
        break
    soma += numeros
    total = numeros
print(f'{total} números foram digitados e a soma entre eles foi {soma}!')