#Cadastro infinito

maiores = 0

while True:
    nome = input("Qual é o seu nome? (ou 'sair' para encerrar) ")
    
    if nome.lower() == "sair":
        break
    
    idade = int(input("Quantos anos você tem? "))
    
    if idade >= 18:
        print("Você é maior de idade! ")
        maiores += 1
    else:
        print("Você é menor de idade! ")
        
    if idade < 16:
        print("Você ainda não pode votar. ")
    elif 16 <= idade < 18 or idade > 70:
        print("Seu voto é opcional. ")
    else:
        print("Seu voto é obrigatório. ")
    
print(f"Total de maiores de idade: {maiores}")