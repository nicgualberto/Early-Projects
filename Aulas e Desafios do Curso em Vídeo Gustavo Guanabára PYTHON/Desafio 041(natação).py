from datetime import date

print("\n=== \033[1;34mNATION SWIMMING CONFEDERATION\033[m ===")
name = str(input("What is your name? "))
year1 = int(input("Year of birth: "))


year2 = date.today().year
idade = year2 - year1

if idade <= 9:
    print(f'You are MIRIM, \033[1;33m{name.upper()}\033[m!')
elif idade <= 14:
    print(f'You are CHILDISH, \033[1;34m{name.upper()}\033[m!')
elif idade <= 19:
    print(f'You are JURNIORES, \033[1;35m{name.upper()}\033[m!')
elif idade <= 25:
    print(f"You are SENIOR, \033[1;36m{name.upper()}\033[m!")
else:
    print(f"You are MASTER, \033[1;37m{name.upper()}\033[m!")
