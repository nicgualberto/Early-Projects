a = ('\033[m',  # 0 - sem cores
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;30'  # 6 - branco
     )


def ajuda(c):
    help(c)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(a[cor], end='')
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)
    print(a[0], end='')


# programa principal
comando = ''
titulo('SISTEMA DE AJUDA PyHELP', 1)
while True:
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ MAIS!', 1)
