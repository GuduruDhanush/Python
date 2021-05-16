import random
import hangman1
import hangman2
from IPython.display import clear_output

print(hangman1.logo, '\n')
stages = hangman1.stages


print('WELCOME TO HANGMAN!!\n')


word_list = hangman2.word_list
lives = 6


# generating random word
random_word = random.choice(word_list)

# print(random_word)

# creating dashlines for random word
dash_lines = []
for _ in random_word:
    dash_lines.append('-')

print(''.join(dash_lines))

# game on

end_of_game = False
while not end_of_game:

    # taking user input
    guess = input('Guess a Letter : ').lower()

    clear_output()

    if guess in dash_lines:
        print(f'You have already in Guessed the letter "{guess}".')

    else:

        # replacing "-" with guessed letter
        for position in range(len(random_word)):
            if random_word[position] == guess:
                dash_lines[position] = random_word[position]

        # punishing for wrong guess and checking for lose condition
        if guess not in random_word:
            print(
                f'You guessed "{guess}", that\'s not in the word. \n You lose a life.')
            print(f'Your remaining lives are "{lives}"')
            if lives == 0:
                end_of_game = True
                print('you lose!')
            else:
                lives -= 1

        print(''.join(dash_lines))

        # checking for win condition
        if '-' not in dash_lines:
            end_of_game = True
            print('you win!')

        print(stages[lives])
