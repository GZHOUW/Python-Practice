file = open("random.txt", "r") # open file
print('The following numbers were read from the randon.txt file:')
count = 0 
sum_numbers = 0
numList = []
for line in file: # iterate over each line
    numList.append(int(line))
    count +=1 # counts the number of numbers in the file
    print(line) # print the numbers
    sum_numbers = int(line) + sum_numbers  # add number to sum in each iteration
print('The lowest number in the list is:',min(numList)) # print minimum number
print('The highest number in the list is:',max(numList))# print maximum number
print('The total of the numbers is:', sum_numbers)# print sum
print('The average of the numbers in the list is:',round(sum_numbers/len(numList),1))#print average

