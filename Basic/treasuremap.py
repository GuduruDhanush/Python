print('WELCOME TO TREASURE MAP!!')

row1 = ['🥲', '🥲', '🥲']
row2 = ['🥲', '🥲', '🥲']
row3 = ['🥲', '🥲', '🥲']

map1 = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

choice = input('Enter your choice from (11,12,13,21,22,23,31,32,33):')

print(choice)

map1[int(choice[0])-1][int(choice[1])-1] = 'X'

print(f"{row1}\n{row2}\n{row3}")
