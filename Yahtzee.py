# Simulating a game of Yahtzee!
# This is a dice game that rolls five dice,
# and gives a score based on what dice were rolled.

# obtain the package for random numbers
import random


def roll_dice():
    # rolls 5 dice, and returns a list of frequencies of each possible value
    # for example, element [3] of the return value is how many 3's appeared
    rolls = [0]*7 # initialize 0 of each (with space for 0)
    results = []
    for i in range(5):
        results.append(random.randint(1, 6))
    for i in range(6):
        rolls[i + 1] = results.count(i + 1)
    return rolls


def reroll_dice(rolls):
    # allows user to reroll dice (extra credit)
    # returns True when the dice is rerolled, and False otherwise
    print('Enter the values of the dice to reroll, separated by spaces')
    print('or enter a blank line to keep the dice as they are.')
    rerolls = input().split()
    if rerolls == []:
        return False
    else:
        print('Rolling', len(rerolls), 'dice')
        for i in rerolls:
            rolls[int(i)] -= 1 # subtract 1 from the old value's frequency
            new_value = random.randint(1, 6)
            rolls[new_value] += 1 # add 1 to the new value's frequency
        rolled = []
        # calculate the value of each dice
        for i in range(len(rolls)):
            if i > 0:
                rolled += rolls[i] * [i]
        print('Re-rolled:', rolled[0], rolled[1], rolled[2], rolled[3], rolled[4])
        return True


def sum_counts(counts):
    # adds up the total of the dice, given the frequencies of each value
    total = 0
    n = 0
    for frequency in counts:
        total += frequency * n
        n += 1
    return total


def three_of_a_kind(counts):
    # returns the total of all dice if at least three match, or zero otherwise
    if 3 in counts:
        return sum_counts(counts)
    return 0


def four_of_a_kind(counts):
    # returns the total of all dice if at least four match, or zero otherwise

    if 4 in counts:
        return sum_counts(counts)
    return 0


def yahtzee(counts):
    # returns 50 if all dice are equal, or zero otherwise
    if 5 in counts:
        return sum_counts(counts)
    return 0


def full_house(counts):
    # returns 30 if there are 2 of one number, and 3 of another
    if (3 in counts) and (2 in counts):
        return 30
    return 0


def small_straight(counts):
    # returns 25 if there are at least 4 consecutive values
    if (0 not in counts[1:5]) or (0 not in counts[2:6]) or (0 not in counts[3:7]):
        return 25
    return 0


def large_straight(counts):
    # returns 30 if there are at least 5 consecutive values
    if (0 not in counts[1:6]) or (0 not in counts[2:7]):
        return 30
    return 0


n = 0
while True:
    # prompt the user to choose to play another round
    if n != 0:
        another = str(input('Another (y/n)?'))
        if another == 'n':
            break
    n += 1
    frequencies = roll_dice()
    rolled = []
    # calculate the value of each dice
    for i in range(len(frequencies)):
        if i > 0:
            rolled += frequencies[i] * [i]
    # print the results
    print('Rolled:', rolled[0], rolled[1], rolled[2], rolled[3], rolled[4])
    # allows the user to reroll dice (extra credit)
    while True:
        reroll = reroll_dice(frequencies)
        if reroll == False:
            break
    print('')
    print('                 Three of a Kind  ', three_of_a_kind(frequencies))
    print('Sets of 1\'s:', frequencies[1] * 1, '  Four of a Kind   ', four_of_a_kind(frequencies))
    print('Sets of 2\'s:', frequencies[2] * 2, '  Full House       ', full_house(frequencies))
    print('Sets of 3\'s:', frequencies[3] * 3, '  Small Straight   ', small_straight(frequencies))
    print('Sets of 4\'s:', frequencies[4] * 4, '  Large Straight   ', large_straight(frequencies))
    print('Sets of 5\'s:', frequencies[5] * 5, '  Yahtzee          ', yahtzee(frequencies))
    print('Sets of 6\'s:', frequencies[6] * 6, '  Chance           ', sum_counts(frequencies))
    print('')
