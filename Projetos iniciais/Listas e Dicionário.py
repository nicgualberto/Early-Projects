#parte de teste da lista de frutas:

frutas = ["Banana", "Melão" , "Uva"]

frutas.append("Abóbora")
frutas.remove("Banana")
print(frutas)
print(len(frutas))

#parte de teste do dicionário:

aluno = {
    "nome": "Nic",
    "idade": 16,
    "curso": "Ciência da Computação"
}

print(aluno["nome"])
print(aluno["idade"])
print(aluno)

#Exercício prático 1

numeros = [1,2,3,4,5]
print(numeros[2])
numeros.append(100)
numeros.remove(5)
print(numeros)

#Exercício prático 2

livro = {
    "titulo": "O homem mais rico da Babilônia",
    "autor": "George S. Clason",
    "ano": 2025,
    "paginas": 230
}

print(livro)

#Lista de dicionários

biblioteca = [
    {"titulo": "O homem mais rico da Babilônia", "autor": "George S. Clason", "ano": 2025},
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899},
    {"titulo": "1984", "autor": "George Orwell", "ano": 1949}
]

print(biblioteca[1]["titulo"])

#tags

livro = {
    "titulo": "1984",
    "autor": "George Orwell",
    "ano": 1949,
    "tags": ["distopia", "política", "ficção"]
}

print(livro["tags"][1])

#Exercício Prático 3

alunos = [
    {"nome": "Nícolas Alves Gualberto", "idade": 17, "nota": [8.5, 9.0, 8.0]},
    {"nome": "Mariana Henerique Paulino do Nascimento", "idade": 17, "nota": [7.0, 7.5, 10.0]},
    {"nome": "Rafael Pereira Martins", "idade": 18, "nota": [10.0, 7.5, 9.0]}
]

print(alunos[1]["nome"])
print(alunos[0]["nota"][1])
alunos[2]["nota"].append(7.5)
print(alunos[2]["nota"])
