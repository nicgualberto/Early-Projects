import random
import json
from pathlib import Path
from datetime import datetime


OPN_REGISTRADA = Path.home() / "registros.json"
userName = input("Crie o seu usuário: @")


print(f"Bem-vindo ao OURCOMUNICATION, \033[1;34m@{userName.upper()}\033[m")

def salvar_registro_json():
    texto = input("Digite o texto que deseja salvar: ").strip()
    data_hora = datetime.now().strftime("\033[1;35m%Y-%m-%d\033[m \033[1;33m%H:%M:%S\033[m")
    
    registro = {
        "usuario": userName,
        "texto": texto,
        "data": data_hora
    }
    
    if OPN_REGISTRADA.exists():
        with open(OPN_REGISTRADA, "r", encoding="utf-8") as arquivo:
            registros = json.load(arquivo)
    
    else:
        registros = []
        
    registros.append(registro)
    
    with open(OPN_REGISTRADA, "w", encoding="utf-8") as arquivo:
        json.dump(registros, arquivo, indent=4, ensure_ascii=False)

    print("A sua opinião foi registrada com sucesso!")
    
def ler_registros_json():
    if not OPN_REGISTRADA.exists():
        print("Ainda não há registros salvos.")
        return
    
    with open(OPN_REGISTRADA, "r", encoding="utf-8") as arquivo:
        registros = json.load(arquivo)
        
    if not registros:
        print("O arquivo está vazio.")
        return
    
    print("\n=== REGISTROS SALVOS ===")
    for i, reg in enumerate(registros, start=1):
        print(f"{i:03} | Usuário: \033[1;32m@{reg['usuario'].upper()}\033[m | Data: {reg['data']} | Texto: {reg['texto']}")
        
def calculadora():
    while True:
            userName1 = str(input("O seu nome de usuário:@ "))
            print(f"Bem-vindo a calculadora, {userName1}!")
            entrar_sair = str(input(f"Você deseja realizar algum cálculo ('sim' para continaur ou 'sair' para encerrar.): "))
            if entrar_sair.lower() == 'sair':
                print(f"Até a próxima, {userName1}!")
                break
            if entrar_sair.lower() == 'sim':
                operacoes = int(input("Escolha uma dessas operações para continuar (Digite os respectivos números > somar'1' subtrair'2' multiplicar'3' dividir'4'): "))
            if operacoes == 1:
                print(f"Boa, {userName1}. Vamos fazer uma soma!")
                n1 = float(input("Digite aqui o primeiro valor: "))
                n2 = float(input("Digite o segundo valor: "))
                soma = n1 + n2
                print(f"O resultado dessa soma é igual a: {soma}")
            if operacoes == 2:
                print(f"Ótimo, {userName1}. Agora iremos realizar uma subtração!")
                n3 = float(input("Digite aqui o primiero valor: "))
                n4 = float(input("Digite o segundo valor: "))
                subtracao = n3 - n4
                print(f"O resultado da subtração é igual a: {subtracao}")
            if operacoes == 3:
                print(f"Isso, {userName1}. Vamos fazer essa multiplicação!")
                n5 = float(input("Digite aqui o seu primeiro valor: "))
                n6 = float(input("Digite o segundo valor: "))
                multiplicacao = n5 * n6
                print(f"A multiplicação entre {n5} e {n6} é igual a: {multiplicacao}")
            if operacoes == 4:
                print(f"Manda bala, {userName1}. É pra já essa divisão!")
                n7 = float(input("Digite aqui seu primeiro valor: "))
                n8 = float(input("Digite o segundo valor: "))
                divisao = n7 / n8
                print(f"O resultado é igual a: {divisao}")
            
def adivinhe():
    print("Bem-vindo ao jogo de adivinhar o número. Você tem 6 tentativas!")
    numero_secreto = random.randint(1, 20)
    tentativas = 6
    while tentativas > 0: 
        try:
            palpite = int(input("Digite seu palpite (1-20): "))
        except ValueError:
            print("Digite um número inteiro, por favor.")
            continue
        
        tentativas -= 1
        
        if palpite == numero_secreto:
            print(f"Você acertou em \033[1;32m{tentativas}\033[m tentativas. Parabéns!")
            break
        elif palpite < numero_secreto:
            print("Você errou. Tente um número maior!")
        elif palpite > numero_secreto:
            print("Você errou. Tente um número menor!")
        if tentativas == 0:
            print("\033[1;31mGAMER OVER\033[m! O número de tentativas esgotou!")
            break

    
def IMC():
    peso = float(input("Digite aqui seu peso: "))
    altura = float(input("Digite aqui sua altura: "))
    IMC = peso / (altura ** 2)
    print("O seu IMC é {:.1f}".format(IMC))

    if IMC < 18.5:
        print("Você está abaixo do peso.")
    elif IMC >= 18.5 and IMC <= 24.9:
        print("Você está com o peso normal.")
    elif IMC >= 25 and IMC <= 30:
        print("Você está com sobrepeso.")
    else:
        print("Você se encontra em estado de obesidade.")
        
def submenu():
    while True:
        print("\n=== FERRAMENTAS DO PROGRAMA ===")
        print("1 - Escreva sua opnião sobre algo que está em alta no \033[1;33mCOLÉGIO DIOCESANO PADRE ROLIM\033[m")
        print("2 - Ler seus registros")
        print("3 - Calculadora")
        print("4 - Jogo do adivinhe um número")
        print("5 - Verificar seu IMC")
        print("6 - Voltar ao menu principal")
        
        escolha = input("Escolha uma opção a seguir(1-6): ")
        
        if escolha == '1':
            salvar_registro_json()
        elif escolha == '2':
            ler_registros_json()
        elif escolha == '3':
            calculadora()
        elif escolha == '4':
            adivinhe()
        elif escolha =='5':
            IMC()
        elif escolha == '6':
            break
        else:
            print("Opção inválida! Tente novamente.")
    
        
def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Ferramentas")
        print("2 - Sobre o programa")
        print("3 - Sair")
    
        escolha = input("Digite aqui o número relacionado a sua respectiva função(1-3): ")
    
        if escolha == '1':
            submenu()
        elif escolha == '2':
            print("O programa foi criado pelo desenvolvedor \033[1;36;40mNícolas Alves Gualberto\033[m.Com efeito de melhorar a comunicação entre o estudante e o sistema de ensino aplicado!Versão 2.0")
        elif escolha == '3':
            print(f"Até mais, \033[1;38m@{userName.upper()}\033[m!")
            break
        else:
            print("Opção inválida. Tente novamente!")
        
menu_principal()