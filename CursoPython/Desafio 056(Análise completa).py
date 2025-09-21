somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulheresmenos = 0
for p in range(1, 5):
    print(f"--- {p}° PESSOA ---")
    nome = str(input("Digite aqui o nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo \033[1;33m[M/F]\033[m: ")).upper().strip()
    somaidade += idade
    if p == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulheresmenos += 1
mediaidade = somaidade / 4
print(f"A média de idade do grupo é de \033[1;36m{mediaidade}\033[m anos!")
print(f"O homem  mais velho do grupo é \033[1;37m{nomevelho}\033[m!")
print(f"A quantidades de mulheres abaixo dos 20 são \033[1;34m{mulheresmenos}\033[m mulheres!")