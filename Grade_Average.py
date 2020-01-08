scoreList = [] # create a list to store the scores entered
while True: # runs repeatedly unless user inputs negative number
    score = int(input('Enter a test score, -1 to get the average: '))
    if score == -1:
        average = sum(scoreList)/len(scoreList) # calculate the average of all scores
        average = round(average,1) # round to one decimal place
        print('The average for all the grade is:', average) # print the result
        break # end the loop
    else:
        scoreList.append(score) # add the input score to the list
