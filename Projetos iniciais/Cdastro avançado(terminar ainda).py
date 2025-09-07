user = str(input("Digite aqui o seu nome de usuário: "))

while True:
   
    aluno = []
    nome = str(input("Digite aqui o nome do aluno (Ou 'sair' para encerrar): "))
    if nome == 'sair':
        print(f"Até mais, {user}!")
        break
    else:
        nota = float(input(f"Digite aqui a nota de {nome}: "))
        aluno.append({"nome":nome, "nota":nota})
    mostra_alunos = len(aluno)
    media = sum(nota) / aluno
    maior = max(nota)
    
print(f"O total de alunos cadastros: {mostra_alunos}")