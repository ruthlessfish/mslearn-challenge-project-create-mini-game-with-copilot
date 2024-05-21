# create game logic for "rock, paper, scissors" game
# Rock beats scissors.
# Scissors beat paper.
# Paper beats rock.

import random

def game():
    score = 0  # initialize score to 0

    while True:  # loop until user chooses to stop playing
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
        # warn the user if the input is invalid
        if user not in ['r', 'p', 's']:
            print('Invalid input')
            continue  # ask for input again

        computer = random.choice(['r', 'p', 's'])

        if user == computer:
            print('It\'s a tie')
        elif is_win(user, computer):
            print('You won!')
            score += 1  # increment score if user wins
        else:
            print('You lost!')

        play_again = input("Do you want to play again? (y/n)\n")
        if play_again.lower() != 'y':
            break  # exit the loop if user doesn't want to play again

    print(f"Your score: {score}")  # display the final score

def is_win(player, opponent):    
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

if __name__ == "__main__":
    game()  # start the game