numbers = []
pairs = []
odd = []

while True:
    try:
        n = int(input('Type a value: '))
        numbers.append(n)
        if n % 2 == 0:
            pairs.append(n)
        else:
            odd.append(n)
            
        choose = int(input('OPITIONS[0-EXIT, 1-CONTINUE]: '))
        
        if choose == 0:
            print(f'Numbers: {numbers}')
            print(f'Pairs: {pairs}')
            print(f'Odd: {odd}')
            break
    except ValueError:
        print(f'Only numbers!')
        