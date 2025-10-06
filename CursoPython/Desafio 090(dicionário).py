print('SCHOOL SYSTEM')

grades = {}
try:
    grades['Name'] = str(input('Type your name: '))
    grades['Grades'] = float(input('Grade: '))

    if grades['Grades'] >= 7.0:
        grades['Situation'] = 'Approved'
    else:
        grades['Situation'] = 'Failed'
        
    for k, v in grades.items():
        print(f'{k} = {v}')
except ValueError:
    print('According to the program')