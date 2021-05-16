import random

print('WELCOME TO ROCK PAPER SCISSORS GAME!')

# initializing

rock = '🤜'
paper = '✋'
scissors = '🤞'

computer = random.choice([rock, paper, scissors])
player = input(
    'Enter your choice (r for rock, p for paper, s for scissors : \n').lower()

# validating user input

if player == 'r':
    you = rock
    print('You : ', you)
    comp = computer
    print('Computer : ', comp)

elif player == 'p':
    you = paper
    print('You : ', you)
    comp = computer
    print('Computer : ', comp)

elif player == 's':
    you = scissors
    print('You : ', you)
    comp = computer
    print('Computer : ', comp)
else:
    you = 'invalid'
    comp = 'invalid'

# checking for tie, win and lose conditions

if (you == rock and comp == rock) or (you == paper and comp == paper) or (you == scissors and comp == scissors):
    print('TIE!!')
elif (you == rock) and (comp == scissors) or (you == scissors) and (comp == paper) or (you == paper) and (comp == rock):
    print('you win!')

elif (you == 'invalid') and (comp == 'invalid'):
    print('you entered invalid input, you lose!')
else:
    print('you lose!')
