scores = list(map(int, input(
    'enter scores side by side with a space between them : ').split()))

heighest_score = 0
for score in scores:
    if score > heighest_score:
        heighest_score = score

print(f'The highest score in the class is: {heighest_score}')
