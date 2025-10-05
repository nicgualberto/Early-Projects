import random
import time
list1 = []
games1 = []

print('-='* 30)
print('			MEGA SENA			')
print('-='*30)
games = int(input('How many games: '))
total = 1
while total <= games:
    cont = 0
    while True:
        shot = random.randint(1, 60)
        if shot not in list1:
            list1.append(shot)
            cont += 1
        if cont >= 6:
            break
        
    list1.sort()
    games1.append(list1[:])
    list1.clear()
    total += 1
print('=='*3, f'DRAFT {games} GAMES', '=='*3)
for i, l in enumerate(games1):
    print(f'Game {i+1}: {l}')
    time.sleep(1)
print('-='*3, 'GOOD LUCK', '-='*3)