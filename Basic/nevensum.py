n = int(input('enter any number: '))

# total = 0
# for evenum in range(2, n+1, 2):
#     total += evenum

# print(f"sum of even numbers in range of {n} is {total}.")

# or

total1 = 0
for evenum in range(1, n+1):
    if evenum % 2 == 0:
        total1 += evenum

print(f"sum of even numbers in range of {n} is {total1}.")
