alunos = [
    {"nome": "Nícolas Alves Gualberto", "idade": 17, "notas": [8.5, 9.0, 8.0]},
    {"nome": "Mariana Henerique Paulino do Nascimento", "idade": 17, "notas": [7.0, 7.5, 10.0]},
    {"nome": "Rafael Pereira Martins", "idade": 18, "notas": [10.0, 7.5, 9.0]}
]

def listar_alunos():
    print("\nLista de alunos:")
    for i, aluno in enumerate(alunos):
        print(f"{i+1} - {aluno['nome']}")
        
def adicionar_nota():
    listar_alunos()
    escolha = int(input("Escolha o número do aluno para adcionar nota: ")) -1
    if 0 <= escolha < len(alunos):
        nova_nota = float(input("Digite a nova nota: "))
        alunos[escolha]["notas"].append(nova_nota)
        print(f"Nota adicionada. Notas atuais: {alunos[escolha]['notas']}")
    else:
        print("Aluno não cadastrado no sistema.")
        
def media_aluno():
    listar_alunos()
    escolha = int(input("Escolha o número do aluno para ver a média: ")) -1
    if 0 <= escolha < len(alunos):
        notas = alunos[escolha]['notas']
        media = sum(notas) / len(notas)
        print(f"Média de {alunos[escolha]['nome']}: {media:2f}")
    else:
        print("Aluno não encontrado no sistema.")
        
while True:
    print("\n=== SISTEMA ESCOLAR ===")
    print("1 - Listar alunos")
    print("2 - Adicionar nota")
    print("3 - Ver média de um aluno")
    print("4 - Sair do sistema")
    
    opcao = input("Escolha uma opção para prosseguir: ")
    
    if opcao == "1":
        listar_alunos()
    elif opcao == "2":
        adicionar_nota()
    elif opcao == "3":
        media_aluno()
    elif opcao == "4":
        print("Saindo do Sistema")
        break
    else:
        print("Opção inválida.Tente novamente!")
