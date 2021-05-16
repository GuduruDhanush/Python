import random
print('WELCOME TO DIGITAL TOSSING!')


toss = random.randint(0, 1)

if toss == 1:
    print('Heads')
elif toss == 0:
    print('Tails')
else:
    pass
