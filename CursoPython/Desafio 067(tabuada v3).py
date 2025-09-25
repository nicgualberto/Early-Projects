print('\n--- \033[1;36mTABUADA V3\033[m ---')

numero = 0

while True:
    numero = int(input('Digite o número que esteja interessado em saber a tabuáda [DIGITE UM VALOR NEGATIVO PARA SAIR DA TABUÁDA] : '))
    if numero < 0:
        break
    for i in range(1, 11):
        resultado = numero * i
        print(f'{numero} x {i} = {resultado}')
print('FIM')
    