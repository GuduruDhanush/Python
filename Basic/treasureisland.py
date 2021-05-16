print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print('WELOME TO TREASURE ISLAND!!')
print('Your Mission is to find the Treasure')

input1 = input(
    'You\'re at crossroad, Whare Do you want to go Right or Left : ').lower()

if input1 == 'left':
    input2 = input(
        'Now You\'ve came to lake, there is a island in the middle of lake, type "Wait" for wait for the boat or type "swim" for swim across: ').lower()

    if input2 == 'wait':
        input3 = input(
            'You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?').lower()

        if input3 == 'yellow':
            print('You found the treasure! You Win!.')
        elif input3 == 'red':
            print('It\'s a room full of fire. "GAME OVER!!".')
        elif input3 == 'blue':
            print('Eaten by Beasts, "GAME OVER!!".')
        else:
            print('"GAME OVER!!".')

    else:
        print('you got attacked by angry trout, "GAME OVER!!".')

else:
    print('you fell into a hole, "GAME OVER!!".')
