people = []
total = 0
women = []

while True:
    register = {}
    register['Name'] = str(input('Name: '))
    register['Gender'] = str(input('Gender[M/F]: ')).upper()
    register['Age'] = int(input('Age: '))
    
    people.append(register.copy())
    total +=1
    
    if register['Gender'] == 'F':
        women.append(register['Name'])
    
    choice = int(input('Choose one option[0 - Break, 1 - Continue]: '))
    
    if choice == 0:
        break

ages = [p['Age'] for p in people]
division = sum(ages) / len(ages)
print('-='*30)
print(f'The total of people registered: {total}.')
print(f'The avarege of the group is {division:.1f} years old.')
print(f'Women of the group: {women}')
print('-='*30)
print('			ABOVE AVAREGE AGE			')
print('-='*30)
for p in people:
    if p['Age'] > division:
        print(f'{p['Name']} is {p['Age']} years old.')
