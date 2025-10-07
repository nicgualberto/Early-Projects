soccer = {}
goals1 = []
tot = 0
time = []

while True:
    soccer['Name'] = str(input('Name of the soccer player: '))
    soccer['Matches'] = int(input('How many matches he played? '))
    goals1.clear()
    for i in range(0, soccer['Matches']):
        goals = int(input(f'Goals in the {i+1}° match: '))
        goals1.append(goals)
    soccer['Goals'] = goals1
    soccer['Total'] = sum(goals1)
    time.append(soccer.copy())
    while True:
        choice = str(input('Do you want to continue[Y/N]: ')).upper()[0]
        if choice in 'YN':
            break
        print('WRONG! Y or N')
        
    if choice == 'N':
        break
print('-='*30)
print('ref		', end='')
for i in soccer.keys():
    print(f'{i:<15}', end='')
print()
print('-='*40)
for i , p in enumerate(time):
    print(f'{i:>3}', end='')
    for d in p.values():
        print(f'{str(d):>15}', end='')
    print()
print('-='*40)

while True:
    search = int(input('Which player do you want to show the data for[999 - break]: '))
    if search == 999:
        break
    if search >= len(time):
        print(f"WRONG! There aren't player with the {search}!")
    else:
        print(f' -- DATA OF THE PLAYER {time[search]["Name"]}: ')
        for i, g in enumerate(time[search]["Goals"]):
            print(f'	In the match {i+1} = {g} goals.')
