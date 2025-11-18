from datetime import date


def voto(ano):
    atual = date.today().year
    if atual - ano >= 18:
        return 'OBRIGATÓRIO'
    elif atual - ano > 70:
        return 'OPCIONAL'
    elif atual - ano >= 16 and atual - ano < 18:
        return 'OPCIONAL'
    else:
        return 'NEGADO'


print('-='*20)
mensagem = voto(ano=int(input('Em que ano você nasceu: ')))
print(mensagem)
