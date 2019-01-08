from random import randint

player_score = 0
computer_score = 0

while player_score < 2 and computer_score < 2:
        print(f'Player score: {player_score} - Computer score: {computer_score}')
        player = input(("Rock, Paper, Scissors... What's your pick!? -> ")).lower()
        random_num = randint(0,2)
        if random_num == 0:
            computer_pick = 'rock'
        elif random_num == 1:
            computer_pick = 'paper'
        else:
            computer_pick = 'scissors'

        if player == computer_pick:
            print(" It's a tie! let's try that again.. ")
        elif player == 'rock':
            if computer_pick == 'paper':
                print(f"Looks like the computer takes this round with it's {computer_pick} pick")
                computer_score += 1
            else:
                print(f'Looks like you take this round with that {player} pick!')
                player_score += 1
        elif player == 'paper':
            if computer_pick == 'scissors':
                print(f"Looks like the computer takes this round with it's {computer_pick} pick")
                computer_score += 1
            else:
                print(f'Looks like you take this round with that {player} pick!')
                player_score += 1
        elif player == 'scissors':
            if computer_pick == 'rock':
                print(f"Looks like the computer takes this round with it's {computer_pick} pick")
                computer_score += 1
            else:
                print(f'Looks like you take this round with that {player} pick!')
                player_score += 1
        else:
                print("Welp.. if you're seeing this something went horribly horribly wrong in the loop")

print(f'The Final score was Player score: {player_score} - Computer score: {computer_score}')
