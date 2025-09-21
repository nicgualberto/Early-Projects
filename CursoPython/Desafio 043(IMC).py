weight = float(input('Please, what is your weight? '))
height = float(input('What is your height? '))

IMC = weight / height ** 2

if IMC < 18.5:
    print('You are underweight!')
elif IMC >= 18.5 and IMC <= 25:
    print('\033[1;32mYou are at your ideal weight!\033[m')
elif IMC >= 25 and IMC <= 30:
    print('You are overweight!')
elif IMC >= 30 and IMC <=40:
    print('You are obese!')
else:
    print("\033[1;31mYou have morbid obesity!\033[m")