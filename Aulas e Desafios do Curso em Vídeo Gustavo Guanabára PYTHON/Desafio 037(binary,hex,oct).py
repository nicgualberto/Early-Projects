name = str(input('What is your name? '))
number = int(input(f'\033[1;36m{name.upper()}\033[m, choose a number: '))
convert = input("""Type - 1 - for binary / Type - 2 - for octal / Type - 3 - for hexadecimal
Now , choose for number class you want: """)


if convert == '1':
    binary = bin(number)[2:]
    print(f'The number typed in \033[1;36mBINARY\033[m number is \033[1;31m{binary}\033[m!')
elif convert == '2':
    octal = f'{number:o}'
    print(f'The \033[1;36mOCTAL\033[m number is \033[1;31m{octal}\033[m!')
else:
    hexadecimal = f'{number:x}'
    print(f'The \033[1;36mHEXADECIMAL\033[m number is \033[1;31m{hexadecimal}\033[m!')

    
    

    