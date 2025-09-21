import random
import time

def jokenpo():
    opcoes = ['rock', 'paper', 'scissors']
    
    print('Options: [0] Rock, [1] Paper, [2] Scissors')
    escolha_usuario = int(input('What is your play? '))
    
    escolha_computador = random.randint(0, 2)
    jogada_computador = opcoes[escolha_computador]
    
    print(f"Your choice: {opcoes[escolha_usuario]}")
    time.sleep(1)
    print(f"The computer choice: {jogada_computador}")
    time.sleep(2)
    
    if opcoes[escolha_usuario] == jogada_computador:
        print("\033[1;33mDRAW\033[m")
    elif (opcoes[escolha_usuario] == 'rock' and jogada_computador == 'scissors') or (opcoes[escolha_usuario] == 'scissors' and jogada_computador == 'paper') or (opcoes[escolha_usuario] == 'paper' and jogada_computador == 'rock'):
        print('\033[1;32mYOU ARE THE CHAMPION!\033[m')
    else:
        print('\033[1;31mTHE COMPUTER WON!\033[m')
        
jokenpo()