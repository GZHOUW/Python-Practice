def falling_distance(time):
    gravity = 9.8
    # calculate distance
    distance = 1 / 2 * gravity * time**2
    return(distance)

print('This program tells you how far an object will fall in a number of seconds.')
while True:
    time = int(input('Enter the falling time in seconds: '))
    # break if the user enters negative value
    if time < 0:
        break
    # call the function
    distance = falling_distance(time) 
    # print result in 1 decimal place
    print('The distance the object will fall in',time,'seconds, is:',round(distance,1),'meters.')
