n = int(input('Enter n: '))
prompt = 'Please enter a unique number between '+str(1)+' and '+str(n)+': '
sum = 0
for i in range(1,n+1):
    sum = sum + i # Find the sum of sequence 1+2+...+n
for j in range(1,n):
    Input = int(input(prompt))
    sum = sum - Input #subtract each number the user inputs
print('The missing number is',sum) # the result of the subtractions is the missing number
