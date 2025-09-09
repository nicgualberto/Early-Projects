userName = input("Digite aqui seu usuário para testar o programa: ")

idade = 18

if idade >= 18:
   print ("Você é maior de idade.")
   
idade1 = 15


if idade1 >= 18:
   print ("Você é maior de idade.")

else:
   print ("Você é menor de idade.")

nota = 85


if nota >= 90:
   print ("Excelente")

elif nota >= 80:
   print ("Muito bom")

elif nota >= 70:
   print ("Bom")

else:
   print ("Precisa melhorar")
   
frutas1 = ["maçã", "banana", "laranja"]

for fruta in frutas1:
    print(fruta)

contador = 0

while contador < 5:

    print(contador)
    contador += 1

    
for i in range(10):

    if i % 2 == 0:
        continue
    print(i)

for i in range(5):
    pass
números = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in números if x % 2 == 0]
print(quadrados)

frutas1.append("pera")
print(frutas1)  

frutas1.insert(1, "uva")
print(frutas1)  


frutas1.remove("banana")
print(frutas1)




fruta_removida = frutas1.pop(2)
print(frutas1)
print(fruta_removida)
frutas1.sort()
print(frutas1)  


frutas1.reverse()
print(frutas1)  
frutas1 = ["maçã", "banana", "laranja"]
print(frutas1[0])
print(frutas1[1])
print(frutas1[2])
print(frutas1[-1])
print(frutas1[-2])
print(frutas1[-3])

ponto = (3, 4)
print(ponto[0])

minha_tupla = (1, 2, 3, 2, 4, 2)
print (minha_tupla.index(2))
print (minha_tupla.index(2, 2))
print (minha_tupla.index(2, 2, 4))

print(ponto[1])
pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}

print(pessoa["nome"])  
print(pessoa["idade"])    
print(pessoa["cidade"])  

pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}


print(pessoa.keys())    
print(pessoa.values())  
print(pessoa.items())  

pessoa.update({"profissao": "Engenheiro"})
print(pessoa)  

frutas = {"maçã", "banana", "laranja"}
numeros = set([1, 2, 3, 4, 5])
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}


uniao = conjunto1 | conjunto2
print(uniao)  


intersecao = conjunto1 & conjunto2
print(intersecao)  


diferenca = conjunto1 - conjunto2
print(diferenca)  


diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)  

frutas = {"maçã", "banana", "laranja"}


frutas.add("pera")
print(frutas)

frutas.remove("banana")
print(frutas)
frutas.discard("uva")
print(frutas)  


frutas.clear()
print(frutas)

def saudacao(nome):
    print(f"Olá, {nome}!")
saudacao("Jão")

def soma(a, b):
    return a + b
resultado = soma(3, 1)
print(resultado)

quadrado = lambda x: x ** 2
print(quadrado(6))

def funcao():
    variavel_local = 10
    print(variavel_local)
    
variavel_global = 20

def funcao2():
    print(variavel_global)
    
funcao()
funcao2()
print(variavel_global)

def area_retangulo(base, altura):
    """
    Calcula a área de um retângulo.
    
    Args:
        base(float): A base do retângulo.
        altura(float): A altura do retângulo
        
    Returns:
        float: A área do retângulo.
    """
    return base * altura
resultado = area_retangulo(3, 4)
print(resultado)
    
def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(soma_variavel(1, 2, 3))
print(soma_variavel(4, 5, 6, 7))

nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))

print("Olá, " + nome + "!")
print(f"Você tem {idade} anos. ")

idade2 = int(input("Digite aqui sua idade: "))

if idade > 16:
    print("Você ainda não pode votar")
else:
    print("Você pode votar")
    
arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

arquivo = open("dados.txt", "w")
arquivo.write("Nícolas, você está evoluindo muito. Orgulhoso pelo seu progresso!")
arquivo.close()

with open("dados.txt", "r") as arquivo:
    conteudo9 = arquivo.read()
    print(conteudo9)
    
import math

resultado = math.sqrt(25)
print(resultado)

from math import sqrt

resultado = sqrt(36)
print(resultado)

import random
import datetime

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)

data_atual = datetime.datetime.now()
print(data_atual)


import meu_modulo
meu_modulo.saudar("João")
resultado = meu_modulo.calcular_soma(5, 3)
print(resultado)

import operacoes
import utilidades

resultado = operacoes.somar(5, 3)
utilidades.imprimir_mensagem(f"O resultado da soma é: {resultado}")

nome = utilidades.obter_nome_usuario()
utilidades.imprimir_mensagem(f"Olá, {nome}!")

from meu_pacote import modulo1, modulo2

modulo1.funcao1()
modulo2.funcao2()