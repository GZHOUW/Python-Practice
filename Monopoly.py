propertyInfo = { # store all the information of properties in a dictionary
    'purple': ['two',2, 50],
    'light blue': ['three',3, 50],
    'maroon': ['three',3, 100],
    'orange': ['three',3, 100],
    'red': ['three',3, 150],
    'yellow': ['three',3, 150],
    'green': ['three',3, 200],
    'dark blue': ['two',2, 200],
} 
    
numberStr = { # to be used to display numbers as strings
    0: 'none',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve'
} 

color = str(input("Which color block will you be building on?"))
money = float(input("How much money do you have to spend?"))
size_str = propertyInfo[color][0] # the number of properties within the group as strings
size_int = propertyInfo[color][1] # the number of properties within the group as integers
cost = propertyInfo[color][2] # the cost of the houses
print('There are', size_str, 'properties and each house costs', cost)
houseNumber = int(money/cost) # total houses that can be built

# Build the houses in two rounds
# In round 1, each peoperty can get at least N number of houses
N = int(houseNumber/size_int)
# There are T number of houses built in round 1
T = size_int*N
# After round 1, there are L number of houses left
L = houseNumber-T
# In round 2, each of the L left over houses will be built on one property
# There will be L number of properties with 1 more house than other properties
# L peoperties get (N+1) houses, and (houseNumber-L) properties get N houses
# display all numbers as strings instead of integers using numberStr dictionary

hotelCost = 5*cost
hotelNumber = int(money/hotelCost)

if money<cost:
    print('You cannot afford even one house.')
elif money < 5*cost:
    if N+1=='none' or L==0:
        print('You can build',numberStr[houseNumber],'house(s) --',
            numberStr[size_int-L], 'will have',numberStr[N])
    elif size_int-L==0 or N==0:
        print('You can build',numberStr[houseNumber],'house(s) --',
            numberStr[L],'will have',numberStr[N+1])
    else:
        print('You can build',numberStr[houseNumber],'house(s) --',
            numberStr[L],'will have',numberStr[N+1],'and',
            numberStr[size_int-L], 'will have',numberStr[N])
else:
    if money>=size_int*hotelCost:
        print(size_str,'will have a hotel')
    elif size_int==2 and hotelNumber==1 and houseNumber!=5:
        print('one will have a hotel and one will have',numberStr[houseNumber-5])
    elif size_int==2 and hotelNumber==1 and houseNumber==5:
        print('one will have a hotel')
    elif size_int==3 and hotelNumber==1 and ((houseNumber-5)%2==0) and (houseNumber-5)/2==0:
        print('one will have a hotel')
    elif size_int==3 and hotelNumber==1 and ((houseNumber-5)%2==0) and (houseNumber-5)/2!=0:
        print('one will have a hotel and two will have',numberStr[(houseNumber-5)/2])
    elif size_int==3 and hotelNumber==1 and ((houseNumber-5)%2!=0):
        print('one will have a hotel and one will have',numberStr[int((houseNumber-5)/2)],'and one will have',numberStr[1+int((houseNumber-5)/2)])
    elif size_int==3 and hotelNumber==2 and houseNumber-10==0:
        print('two will have a hotel')
    elif size_int==3 and hotelNumber==2 and houseNumber-10!=0:
        print('two will have a hotel and one will have',numberStr[houseNumber-10])

        
