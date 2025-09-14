nome = str(input("Digite aqui seu nome: "))
if nome == 'Nícolas':
    print('Que nome bonitão!')
elif nome == 'Mariana':
    print('Nome de pessoa gata')
elif nome in ['Rafael', 'Laura', 'Giovana', 'Júlia', 'Levi', 'Tamila']:
    print('Seu nome é bem interessante!')
else:
    print('Seu nome é bem normal')
print(f'Tenha um bom dia, {nome}!')