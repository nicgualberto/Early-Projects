numbers = []

while True:
    numbers.append(int(input('Type a value: ')))
    
    choose = int(input('Do you want to continue typing numbers or exit [1-continue 2-print the list 0-exit]'))
    
    if choose == 0:
        print('See you later!')
        break
    
    elif choose == 2:
        numbers.sort()
        print(numbers)
        break