list1 = [[], []]
value = 0

for c in range(1,8):
    value = int(input('Type a value: '))
    
    if value % 2 == 0:
        list1[0].append(value)
    else:
        list1[1].append(value)

print(f'The pairs numbers {list1[0]}')
print(f'The odd numbers {list1[1]}')
