product = str(input('What product do you wanna buy? '))
price = float(input('Price: R$ '))
options = input("What's payment method? (Type '1' in cash(10% off) , '2' one-time payment(%5 off), '3' double charge(Normal price) and '4' triple charge or more(25% interest rate): ")

if options == '1':
    new_price = price - (price * 0.10)
    print(f"The value of the \033[1;37m{product.upper()}\033[m: \033[1;32mR${new_price :.2f}\033[m!")
elif options == '2':
    new_price2 = price - (price * 0.05)
    print(f"The value of the \033[1;37m{product.upper()}\033[m: \033[1;32mR${new_price2 :.2f}\033[m!")
elif options == '3':
    print(f"The value of the \033[1;37m{product.upper()}\033[m: \033[1;32mR${price :.2f}\033[m!")
else:
    new_price3 = price + (price * 0.25)
    print(f"The value of the \033[1;37m{product.upper()}\033[m: \033[1;32mR${new_price3 :.2f}\033[m!")