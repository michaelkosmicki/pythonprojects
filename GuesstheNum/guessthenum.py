import random

random_number = random.randint(1,10)
guess = None

while True:
    guess = input("Pick a number from 1 to 10: ")
    guess = int(guess)
    if guess < random_number:
        print("Too Low")
    elif guess > random_number:
        print("Too High")
    else:
        print("You Won!")
        play_again = input("Would you like to try again? (y/n) ")
        if play_again == "y":
            guess = input("Pick a number from 1 to 10: ")
            guess = int(guess)
        else:
            print("Cool, see ya next time!")
            break
