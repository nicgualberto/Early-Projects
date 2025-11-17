# função de contagem
import time

def count(inicio, fim, passo):
    print('-=' * 20)
    print('Contagem de 1 até 10 de 1 em 1: ')
    for i in range(1, 11):
        print(i) 
        time.sleep(0.5)
    print('FIM')
    print('-=' * 20)
    print('Contagem de 10 até 0 de 2 em 2: ')
    for n in range(10, -2, -2):
        print(n)
        time.sleep(0.5)
    print('FIM')
    print('-=' * 20)
    print('Agora é sua vez de personalizar sua contagem: ')
    print('-=' * 20)
    print(f'CONTAGEM DE {inicio} ATÉ {fim} DE {passo} EM {passo}')
    for p in range(inicio, fim, passo):
        print(p )
        time.sleep(0.5)
    print('FIM')


#programa
print('CONTAGEM')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
count(inicio, fim, passo)