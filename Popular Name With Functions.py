# input a file name, and returns a list of names
def get_names_list(fileName):
    file = open(fileName, "r") # open and read the file
    name_list = [] # create lists to contain the names
    # iterate over each line
    for line in file:
        name_list.append(line[0:-1]) # add the names to list, without adding '\n'
    return name_list

# inputs a name and a list of names, and returns the rank of that name
def check_name(name, name_list):
    if name in name_list:
        rank = name_list.index(name) +1 # find the rank of the name
    else:
        rank = 0
    return rank

print('Enter a name to see if it is a popular girls or boys name.')
while True: # runs forever until user inputs 'stop'
    print('') # a blank line as separation 
    name = str(input('Enter a name to check, or "stop" to stop: '))
    if name == 'stop':
        break # exit the loop
    else:
        # call both functions to get the rank of names
        boyRank = check_name(name, get_names_list('BoyNames.txt'))
        girlRank = check_name(name, get_names_list('GirlNames.txt'))
        # print the results
        if boyRank != 0:
            print(name,'is a popular boys name and is ranked', boyRank,'.')
        else:
            print(name,'is not a popular boys name.')
        if girlRank != 0:
            print(name, 'is a popular girls name and is ranked', girlRank,'.')
        else:
             print(name, 'is not a popular girls name.')
