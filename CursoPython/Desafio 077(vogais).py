texto = ('Palavra',
         'Nicolas',
         'Mariana',
         'Objeto',
         'Correr',
         'Teclado',
         'Mouse')
for palavra in texto:
    print(f'Na palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')