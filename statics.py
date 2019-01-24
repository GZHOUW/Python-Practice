#A group of statisticians at a local college has asked you to create a set of functions that compute the median and mode of a set of numbers. Define these functions, median and mode, in a module named stats.py. Also include a function named mean, which computes the average of a set of numbers. Each function should expect a list of numbers as an argument and return a single number. Each function should return 0 if the list is empty. Include a main function that tests the three statistical functions with a given list.

def mean(list1):
    if len(list1) == 0:
        return(0)
    else:
        mean = sum(list1) / len(list1)
        return(mean)


def median(list1):
    if len(list1) == 0:
        return(0)
    else:
        list1.sort()
        if len(list1) % 2 == 0:
            median = (list1[int(len(list1)/2 - 1)] + list1[int(len(list1)/2)])/2
            return(median)
        else:
            return(list1[int((len(list1)-1)/2)])
        
def mode(list1):
    if len(list1) == 0:
        return(0)
    else:
        list1.sort()
        lists = [[] for _ in range(len(list1))]
        for empty_list in lists:
            for number in list1:
                if len(empty_list) == 0 and number != None:
                    empty_list.append(number)
                    list1[list1.index(number)] = None
                elif (number in empty_list) == True and number != None:
                    empty_list.append(number)
                    list1[list1.index(number)] = None
                elif (number in empty_list) == False and number != None:
                    lists[lists.index(empty_list)+1].append(number)
                    list1[list1.index(number)] = None
                    break
        occurrence = []
        for element in lists:
            occurrence.append(len(element))
        mode = lists[occurrence.index(max(occurrence))][0]
        return(mode)


def main(List):
    print('List:', List)
    print('Median:', median(List))
    print('Mean:', mean(List))
    print('Mode:', mode(List))

main([3,1,7,1,4,10])
