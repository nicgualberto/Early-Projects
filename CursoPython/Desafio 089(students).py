students = []
while True:
    try:
        name = str(input('Name: ')).upper()
        note1 = float(input('Note1: '))
        note2 = float(input('Note2: '))
        media = (note1 + note2) / 2
        students.append([name, [note1, note2], media])
        
        choose = str(input('Do you wanna continue[Y/N]: ')).upper()
        
        if choose == 'N':
            break
    except ValueError:
        print('According of the sugested!')
print(f'{"No.":<4}{"NAME":<10}{"MEDIA":>8}')
print('-'*26)
for i, s in enumerate(students):
    print(f'{i:<4}{s[0]:<10}{s[2]:>8.1f}')
while True:
    print('-'*35)
    choice = int(input('Show the notes of what student? (999 break): '))
    if choice == 999:
        break
    if choice <= len(students) - 1:
        print(f'Notes {students[choice][0]} {students[choice][1]}')
print('COME BACK LATER!')