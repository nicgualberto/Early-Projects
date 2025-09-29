dezoitomais = 0
homens = 0
mulheresmenos20 = 0

while True:
    idade = int(input('Digite aqui a idade: '))
    sexo = str(input('Digite aqui o sexo [M/F]: ')).upper()

    if idade > 18:
        dezoitomais += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresmenos20 += 1

    escolha = str(input('Você deseja cadastrar mais alguma pessoa [Y/N]: ')).upper()
    if escolha == 'N':
        break
    
print(f'{dezoitomais} pessoas têm mais de 18 anos. {homens} homens foram cadastrados. E {mulheresmenos20} mulheres têm menos de 20 anos!')
