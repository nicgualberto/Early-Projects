name  = str(input('Type your username: @'))
number1 = int(input(f'\033[1;36m@{name}\033[m, choose a number: '))
number2 = int(input('Other number: '))

if number1 > number2:
    print(f" \033[4;33m{number1}\033[m is bigger than \033[4;34m{number2}\033[m! ")
elif number1 < number2:
    print(f" \033[4;33m{number2}\033[m is bigger than \033[4;34m{number1}\033[m! ")
else:
    print(f" \033[1;36m{number1}\033[m is the same \033[1;36m{number2}\033[m!") 