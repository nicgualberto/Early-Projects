def fatorial(num=1, show=False):
    """
    -> Função para calcular o fatorial de um número;
    num = numero a ser calculdo.
    show = (opcional) mostra o cálculo ou não.
    return = o valor do fatorial.
    """
    resultado = 1
    for i in range(1, num + 1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        resultado *= i
    return resultado


print('-='*20)
mensagem = fatorial(int(input('Número: ')), show=False)
print(mensagem)
