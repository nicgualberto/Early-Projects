print("\n=== \033[1;35;47mSCHOOL SYSTEM\033[m ===")
name = str(input("What's your name? "))
test1 = float(input("What was your score on the first \033[1;36mEXAM\033[m? "))
test2 = float(input("And on the second: "))

media = (test1 + test2) / 2

if media < 5.0:
    print(f"\033[1;37m{name.upper()}\033[m, you are \033[1;31mFAILED\033[m!")
elif media >= 5.0 and media <= 6.9:
    print(f"\033[1;37m{name.upper()}\033[m, you are \033[1;33mRECOVERING\033[m!")
else:
    print(f"\033[1;37m{name.upper()}\033[m, you are \033[1;32mAPPROVED\033[m!")
    