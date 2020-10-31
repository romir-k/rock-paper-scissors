import random

options = ['rock', 'paper', 'scissors']
num = int(input('How many games would you like to play: '))


def game():
    computer_score = 0
    your_score = 0
    for _ in range(num):
        ans = random.choice(options)
        inp = input('Rock, paper, or scissors: ')
        iss = inp.lower()
        if ans == 'paper' and iss == 'rock':
            print('Computer chose paper. You lose.')
            computer_score += 1
        elif ans == 'paper' and iss == 'scissors':
            print('Computer chose paper. You win!')
            your_score += 1
        elif ans == 'rock' and iss == 'paper':
            print('Computer chose rock. You win!')
            your_score += 1
        elif ans == 'rock' and iss == 'scissors':
            print('Computer chose rock. You lose.')
            computer_score += 1
        elif ans == 'scissors' and iss == 'rock':
            print('Computer chose scissors. You win!')
            your_score += 1
        elif ans == 'scissors' and iss == 'paper':
            print('Computer chose scissors. You lose.')
            computer_score += 1
        elif ans == iss:
            print('Draw')
        else:
            print('Error')
    return "Your score is " + str(your_score) + '\n' + "The computer's score is " + str(
        computer_score)  # Return outside of the loop


print(game())
