# welocme message
print('WELCOME TO BMI CALCULATOR!!')

# asking for user input
height = float(input('enter your height in m: '))
weight = float(input('enter your weiht in kg: '))

# calculating bmi
bmi = round(weight/height ** 2)
print(f'your bmi is {bmi}.')

# checking with conditions
if bmi < 18.5:
    print('underweight')
elif bmi < 25:
    print('normal weight')
elif bmi < 30:
    print('overweight')
elif bmi < 35:
    print('obese')
else:
    print('clinically obese')

print('bye, have a nice day!!')
