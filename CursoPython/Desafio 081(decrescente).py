count = 0
numbers = []

while True:
    try:
        n = (int(input('Add a value in the list: ')))
        numbers.append(n)
        count += 1
        
        choose = int(input('OPITIONS[0 - exit , 1 - continue]: '))

        if choose == 0:
            numbers.sort(reverse=True)
            print(f'They were typed {count} in the list')
            print(f'List in descending order : {numbers}')
            if not 5 in numbers:
                print(f"The number 5 isn't in the list")
            else:
                print("The number 5 is in the list!")
            break
    except ValueError:
        print('Only numbers!')
