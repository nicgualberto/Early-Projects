soccer = {}
goals1 = []
tot = 0

soccer['Name'] = str(input('Name of the soccer player: '))
soccer['Matches'] = int(input('How many matches he played? '))

for i in range(0, soccer['Matches']):
    goals = int(input(f'Goals in the {i+1}° match: '))
    goals1.append(goals)
    soccer['Goals'] = goals1
    soccer['Total'] = sum(goals1)
print('-='*30)
print(soccer)
print('-='*30)

for k, v in soccer.items():
    print(f'{k} = {v}')
print('-='*30)

print(f'The soccer player {soccer['Name']} played {soccer['Matches']} match!')
for i in range(0, soccer['Matches']):
    print(f'=> In the {i+1}° match , goals = {goals1[i]} ')
print(f'Total of the goals: {soccer['Total']}')


    

    