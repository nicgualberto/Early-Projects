frase = str(input("Digite uma frase que vinher na sua cabeça: ")).strip().upper()
print(frase)
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'Temos um palíndromo! O inverso de {junto} é {inverso}')
else:
    print("A frase digitada não é um palíndromo!")