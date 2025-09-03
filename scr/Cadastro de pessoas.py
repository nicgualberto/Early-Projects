#Cadastro de pessoas
maiores = 0

for i in range(5):
    nome = input("Qual é o seu nome? ")
    idade = int(input("Quantos anos você tem? "))

    if idade >= 18:
        print("Você é maior de idade.")
        maiores += 1
    elif idade < 18:
        print("Você é menor de idade.")
        
    if idade < 16:
        print("Você ainda não pode votar!")
    elif 16 <= idade < 18 or idade > 70:
        print("Seu voto é opcional.")
    else:
        print("Seu voto è obrigatório!")
        
print(f"A quantidade de maiores idades cadastrados é: {maiores} ")
                
                
          
            