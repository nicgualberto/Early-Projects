user = str(input("Digite aqui o seu nome de usuário: "))
aluno = []
while True:
   
    nome = input("Digite aqui o nome do aluno (Ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        print(f"Até mais, {user}!")
        break
    else:
        nota = int(input(f"Digite aqui a nota de {nome}: "))
        aluno.append({"nome":nome, "nota":nota})
if aluno:
    mostra_alunos = len(aluno)
    media = sum(a["nota"] for a in aluno) / mostra_alunos
    maior = max(aluno, key=lambda x: x["nota"])
print(f"O total de alunos cadastros: {mostra_alunos}")
print(f"A média da turma: {media:.1f}")
print(f"Maior nota: {maior['nome']} com {maior['nota']}")
print("Alunos acima da média: ")
for a in aluno:
    if a["nota"] > media:
        print(f" - {a['nome']} ({a['nota']})")
