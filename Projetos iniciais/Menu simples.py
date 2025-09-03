#Exercício 

nome = input("Qual é o seu nome? ")
idade = int(input("Quantos anos você tem? "))

print(f"Olá, {nome}! Você tem {idade} anos. ")

if idade >= 18:
    print("Você é maior de idade.")
elif idade < 18:
    print("Você é menor de idade.")
    
if idade >= 16:
    print("Você já pode votar!")
elif 16 <= idade < 18 or idade > 70:
    print("seu voto é opcional")
else:
    print("Você ainda não pode votar!")
  


