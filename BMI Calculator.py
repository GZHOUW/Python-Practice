# Let user input the height and the weight
height = float(input('Enter your height in inches: '))
weight = float(input('Enter your weight in pounds: '))
# Compute BMI using the given formula
BMI = round(weight * 703 / height**2, 1)
print('Your BMI is: ', BMI)
# For different BMI, the user can be underweight, optimal weight, or overweight. 
if BMI < 18.5:
    print('Your BMI indicates that you are underweight.')
elif BMI <= 25 and BMI >= 18.5:
    print('Your BMI indicates that you are optimal weight.')
elif BMI > 25:
    print('Your BMI indicates that you are overweight.')

