tupla1 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte', 'sair')
while True:
    print(tupla1[int(input('Digite o número que você pretende ler( 0 - 20 ): '))])
    
    escolha = int(input('Você deseja continuar no programa ou sair(1 - para continuar e 21 - sair): '))
    if escolha == 21:
        break
