print('\n=== \033[1;32mENLISTMENT SEVICE\033[m ===')
name = str(input('What is your name: '))
age = int(input('Please, informe your age: '))

if age > 18:
    print(f"\033[1;37m{name.upper()}\033[m, It's about time your enlisted! ")
elif age < 18:
    print(f"Your time still come!")
else:
    print('\033[1;32mNow is your time!\033[m')

