numberList = [] # create a list to store the scores entered
while True: # runs repeatedly unless user inputs negative number or error occurs
    try:
        number = int(input('Enter a positive number to total or a negative number to calculate average: '))
    # handle Value Error
    except ValueError:
        print('What you entered was not a valid number. Try again.')
    if number < 0:
        total = sum(numberList) # calculate total
        try:
            average = total / len(numberList) # calculate the average of all scores
            average = round(average,1) # round to one decimal place
            print('The average of the numbers is:', average) # print the result
            print('The sum of the numbers is:', total)
            break # end the loop
        # handle ZeroDivisionError
        except ZeroDivisionError:
            print('You did not enter any numbers to average.')
            break # end the loop
    else:
        numberList.append(number) # add the input number to the list
