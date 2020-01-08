# prompt user input
tempCelsius = int(input('Enter the number of celsius temperatures to display: '))
print('Celsius','   ','Fahrenheit') # print the first row of the table
for Celsius in range(0,tempCelsius+1): # loop from 0 to the desired temperature
    Fahrenheit = 9 / 5 * Celsius + 32 # convert Celsius to Fahrenheit
    Fahrenheit = round(Fahrenheit, 1) # round the temperature to one decimal place
    if Celsius < 10:
        print(Celsius,'         ', Fahrenheit)
    else:
        print(Celsius,'        ', Fahrenheit) # allign the data in one column
