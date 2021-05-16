heights = list(map(int, input(
    'enter heights side by side with a space between them : ').split()))
total = 0
count = 0
for height in heights:
    total += height
    count += 1

avgh = total/count
print(round(avgh))
