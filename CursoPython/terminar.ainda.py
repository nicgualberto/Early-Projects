soccer = {}
goals1 = []
tot = 0
while True:
    soccer['Name'] = str(input('Name of the soccer player: '))
    soccer['Matches'] = int(input('How many matches he played? '))

    for i in range(0, soccer['Matches']):
        goals = int(input(f'Goals in the {i+1}° match: '))
        goals1.append(goals)
        soccer['Goals'] = goals1
        soccer['Total'] = sum(goals1)
        
        choice = int(input('Choose one options[0 - Break 1 - Continue]: '))
        
        if choice == 0:
            break
#    print('-='*30)

asprint(f'The soccer player {soccer['Name']} played {soccer['Matches']} match!')
for i in range(0, soccer['Matches']):
    print(f'=> In the {i+1}° match , goals = {goals1[i]} ')
print(f'Total of the goals: {soccer['Total']}')