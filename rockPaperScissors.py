#rock paper scissors
import random
player = int(input('enter 0-rock,1-scissors,2-paper '))
if player == 0:
    player = 'rock'
elif player == 1:
    player = 'scissors'
else:
    player = 'paper'

computer = random.randint(0,2)
if computer == 0:
    computer = 'rock'
elif computer == 1:
    computer = 'scissors'
else:
    computer = 'paper'

# r>s,s>p,p>r
if player == 'rock' and computer =='scissors':
    print(f'win! {player} beats {computer}')
elif player == 'scissors' and computer == 'paper':
    print(f'win! {player} beats {computer}')
elif player == 'paper' and computer == 'rock':
    print(f'win! {player} beats {computer}')
elif player == computer:
    print(f'draw! {player} and {computer}')
else:
    print(f'lose! {computer} beats {player}')

