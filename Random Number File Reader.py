file = open("random.txt", "r") # open file
print('The following numbers were read from the randon.txt file:')
count = 0 
sum_numbers = 0 
for line in file: # iterate over each line
    count +=1 # counts the number of numbers in the file
    print(line) # print the numbers
    sum_numbers = int(line) + sum_numbers  # add number to sum in each iteration
print('The total of the numbers is:', sum_numbers)
print('The file contained', count, 'numbers.')

