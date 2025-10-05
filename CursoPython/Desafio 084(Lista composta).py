temp = []
princ = []
maxi = mini = 0
while True:
    temp.append(str(input('Name: ')))
    temp.append(float(input('Weight: Kg ')))
    if len(princ) == 0:
        maxi = mini = temp[1]
    else:
        if temp[1] > maxi:
            maxi = temp[1]
        if temp[1] < mini:
            mini = temp[1]
    princ.append(temp[:])
    temp.clear()
    
    choose = str(input('Do you want to continue[Y/N]: ')).upper()
    
    
    
    if choose == 'N':
        print('See you later!')
        break
print('-=' * 30)
print(f'The quantity of people registered in the list: {len(princ)} ')
print(f'The heavy weight was {maxi}Kg:')
for p in princ:
    if p[1] == maxi:
        print(f'{p[0]}')
print('--' * 30)
print(f'The light weight was {mini}Kg:')
for p in princ:
    if p[1] == mini:
        print(f'{p[0]}')
print('--' * 30)
print('END')