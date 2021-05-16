print('WELOME TO LOVE CALCULATOR!!')

name1 = input('Enter your Name: ').lower()
name2 = input('Enter your Lover Name: ').lower()
name3 = name1 + name2

true = name3.count('t') + name3.count('r') + \
    name3.count('u') + name3.count('e')
love = name3.count('l') + name3.count('o') + \
    name3.count('v') + name3.count('e')

love_score = int(str(true) + str(love))


if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
