import random
import time

play = {}
tot = 0
play['Player 1'] = random.randint(1, 6)
play['Player 2'] = random.randint(1, 6)
play['Player 3'] = random.randint(1, 6)
play['Player 4'] = random.randint(1, 6)

print('-='*30)
print('		DICE OF THE PLAYERS		')
print('-='*30)


for k, v in play.items():
    time.sleep(0.5)
    print(f'{k} take out {v}')
    

print('--'*30)
print('			RANKING			')
print('--'*30)

sequence = sorted(play.items(), key=lambda x: x[1], reverse=True)


for c, i in sequence:
    tot += 1
    time.sleep(1)
    print(f'{tot}° Lugar: {c} with {i}')

#print(f'The winner is \033[1;32m{max(play)}\033[m!')