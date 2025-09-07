turma = []
while True:
    nota = float(input("Digite aqui a nota: (Ou '-1' para encerrrar): "))
    if nota == -1:
        print("Até mais!")
        break
    else:
        turma.append(nota)
total_alunos = len(turma)
media = sum(turma) / total_alunos
maior = max(turma)
menor = min(turma)

acima_media = 0
for n in turma:
    if n > media:
        acima_media += 1
print(f"\nO total de notas adicionadas : {total_alunos}")
print(f"A média da turma : {media:.1f}")
print(f"A nota acima da média: {maior}")
print(f"A menor nota: {menor}")
print(f"Alunos acima da média: {acima_media}")