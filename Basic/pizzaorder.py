print('WELCOME TO PYTHON PIZZA!!')

print('Menu \nS = small pizza = $15 \nM = medium pizza = $20 \nL = large pizza = $25')
user_input = input('Please order from S,M and L : ').upper()
bill = 0

if user_input == 'S':
    bill = 15

    pep = input('want pepperoni on pizza? it will cost $2, Y or N? : ').upper()
    if pep == 'Y':
        bill += 2

elif user_input == 'M':
    bill = 20

    pep = input('want pepperoni on pizza? it will cost $3, Y or N? : ').upper()
    if pep == 'Y':
        bill += 3

elif user_input == 'L':
    bill = 25

    pep = input('want pepperoni on pizza? it will cost $3, Y or N? : ').upper()
    if pep == 'Y':
        bill += 3

cheese = input('want cheese on pizza? it will cost $1, Y or N? : ').upper()
if cheese == 'Y':
    bill += 1

print(f'your final bill is ${bill}')

print('Enjoy your pizza!!')
