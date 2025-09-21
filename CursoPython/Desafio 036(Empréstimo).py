print("\n=== \033[4;36mEMPRÉSTIMO BANCÁRIO\033[m ===")
userName = str(input('Digite seu nome: '))
valor_da_casa = float(input(f'\033[1;33m{userName.upper()}\033[m, qual será o valor da casa a ser comprada? '))
salario = float(input('Nos forneça também, qual o seu salário? R$ '))
anos = int(input('Em quantos anos o senhor pretende quitar o valor da casa? '))

parcela = valor_da_casa / (anos * 12)

if parcela >= 0.3 * salario:
    print(f'\033[1;33m{userName.upper()}\033[m o empréstimo solicitado será negado por saldo insuficiente!')
else:
    print(f'Empréstimo solicitado com sucesso, \033[4;33m{userName.upper()}\033[m! O valor da prestação é R${parcela:.2f} por mês durante {anos}.')

