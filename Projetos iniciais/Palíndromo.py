frase = str(input("Digite aqui sua frase: ").lower()).replace(" ","")
print(frase)
frase_invertida = frase[::-1]
if frase == frase_invertida:
    print("Essa frase é um palíndromo!")
else:
    print("Essa frase não é um palíndromo.")