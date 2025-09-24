userName = str(input('Qual é o seu nome? ')).upper()
sexo = str(input('Digite aqui seu sexo \033[1;36m[M/F]\033[m: ')).upper()
while sexo not in ['M', 'F']:
    print(f'Por favor, {userName}, digite um dos valores aceitos: \033[1;35m[M/F]\033[m')
    sexo = str(input('Digite aqui seu sexo \033[1;36m[M/F]\033[m: ')).upper()

print('\033[1;34mOBRIGADO! Você contribuiu muito para a pesquisa que estamos realizando.\033[m')
   