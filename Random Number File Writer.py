import random
print('This program writes random numbers to the random.txt file')
file = open("random.txt","w+") # create txt file
iteration = int(input('How many numbers would you like to write: '))
for i in range(iteration):
    number = random.randint(1,500) # create random number
    file.write(str(number) + '\n') # write that number to the file
print(iteration,'numbers were written to the random.txt file')
file.close()
