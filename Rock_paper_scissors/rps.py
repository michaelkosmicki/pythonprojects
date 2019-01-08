import random

print('Would you like to play a game of rock, paper, scissors?')
answer = input()
if answer[0] == 'y':
    print('ok cool')
else:
    print("Fine I'll play with someone else!")
    exit()
print("Lets do this! What's your pick?")
user_pick = input()
computer_pick = random.randint(1,3)
if computer_pick == 1:
    computer_pick = 'rock'
elif computer_pick == 2:
    computer_pick = 'paper'
elif computer_pick == 3:
    computer_pick = 'scissors'
else:
    print('Something went Horribly wrong please help!')
    exit()
if computer_pick == 'scissors' and user_pick == 'rock':
    print(f'Nice work! {user_pick} beats {computer_pick} ')
elif computer_pick == 'rock' and user_pick == 'scissors':
    print(f'Sorry {computer_pick} beats {user_pick}')
elif computer_pick == 'paper' and user_pick == 'rock':
    print(f'Sorry {computer_pick} beats {user_pick}')
elif computer_pick == 'scissors' and user_pick == 'paper':
    print(f'Sorry {computer_pick} beats {user_pick}')
elif computer_pick == 'rock' and user_pick == 'paper':
    print(f'Nice work! {user_pick} beats {computer_pick} ')
elif computer_pick == 'paper' and user_pick == 'scissors':
    print(f'Nice work! {user_pick} beats {computer_pick} ')
else:
    print(f'Looks like you both picked {user_pick}')
print("Well that's all she wrote, see you next time!")
