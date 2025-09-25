
numeros = int(input('Digite um valor [999 para parar]: '))
soma = 0
while numeros != 999:
    soma += numeros
    total = numeros
    numeros = int(input('Digite outro valor: [999 para parar]: '))
print(f'{total} números foram digitados e a soma entre todos eles foi: {soma} ')