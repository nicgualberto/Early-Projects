def media (nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


def dobro(num):
    return num * 2

while True:
    print("\n=== NÚMEROS ===")
    print("1 - Calcular o dobro de um número")
    print("2 - Calcular a média de três números")
    print("3 - Sair do programa")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        num = float(input("Digite um número, chefe: "))
        print(f"O dobro de {num} é {dobro(num)}")
                    
    elif opcao == "2":
        numb1 = float(input("Digite seu primeiro número: "))
        numb2 = float(input("Digite seu segundo número: "))
        numb3 = float(input("Digite seu terceiro número: "))
        print(f"A média dos números é {media(numb1, numb2, numb3)} ")

    elif opcao == "3":
        print("Saindo do programa.")
        break
                    
    else:
        print("Opção inválida!Tente novamente.")
