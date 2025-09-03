#Desafio 01 /Contagem de um número par:

numero = int(input("Digite um número: "))

for i in range(1, numero + 1):
    if i % 2 == 0:
        print(i)

#Desafio 02 /Programa para votar

idade = int(input("Digite sua idade: "))

if idade >= 16:
    print("Você pode votar!")
else:
    print("Você, por equanto, não pode votar!")
    
#Desafios 03 /Cont

numero = int(input("Qual número você quer na tabuáda? "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")

#Desafios 04 /Contador inverso
    
numero = int(input("Digite um número de sua escolha: "))

for i in range(numero, 0, -1):
    if i % 2 !=0:
        print(i)
      
