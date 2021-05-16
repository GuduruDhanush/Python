import random
print('Put your cards in the box.')

names = input('Enter your names: ')

names_list = names.split()

# num = random.randint(0, len(names_list))

# print(f"{names_list[num]} is going to buy the meal today!")

print(f"{random.choice(names_list)} is going to buy the meal today!")
