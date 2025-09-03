alunos = [
    {"nome":"Olívio", "nota": 7.0},
    {"nome":"Nícolas", "nota": 6.0},
    {"nome":"Rafael", "nota": 8.0}
]

for aluno in alunos:
    if aluno["nota"] >= 7:
        print(aluno["nome"], "foi aprovado!")
    else:
        print(aluno["nome"], "foi reprovado!")
        

atletas = [
    {"nome": "Nícolas", "pontos": 30},
    {"nome": "Mariana", "pontos": 20},
    {"nome": "Oliver", "pontos": 15}
]

for atleta in atletas:
    if atleta ["pontos"] >= 18:
        print(atleta["nome"], "você é uma estrela do voleibol!")
    elif atleta ["pontos"] >= 30:
        print(atleta["nome"], "você é expecional!")
    else:
        print(atleta["nome"], "você precisa melhorar!")
        
        
