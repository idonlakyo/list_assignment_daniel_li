"""
-------------------------------------------------------------------------------
Name:		Li_Daniel_list_assignment.py
Purpose:    List Assignment

Author:		Li. D

Created:		26/04/2017
------------------------------------------------------------------------------
"""

def two23(numlist):
    """
    Takes a list of numbers and returns True if there are two 2's or three 3's
    :param numlist: A list of integers
    :return: True or False
    """

    # Initialize counter variables for the number of 2's and the number of 3's
    num_twos = 0
    num_threes = 0

    # Using a loop to check if each number in the list is a 2 or a 3
    for i in numlist:

        # Checking if the number is a 2 or 3, and adding 1 to the respective counter if so
        if i == 2:
            num_twos += 1
        elif i == 3:
            num_threes += 1

    # Checking if the number of 2's is two and the number of 3's is three and returning True of False based on this
    if num_twos == 2 or num_threes == 2:
        return True
    else:
        return False

def after4(numlist):
    """
    Takes a list of integers and removes everything before the last 4 in the list
    :param numlist: a list of integers
    :return: a new list of integers with everything after the last 4 in the original list
    """

    # Using a loop to find the last 4 in the list and creating a new list that has the values after the 4
    for i in range(len(numlist)-1, 0, -1):
        if numlist[i] == 4:
            new_list = numlist[i+1:]

            # Returning the list of values after the last 4
            return new_list

def closeby2(nums1, nums2):
    """
    Takes two list and returns the number of times the values with the same index are within 2 of each other
    :param nums1: A list of integers with the same length as nums2
    :param nums2: A list of integers with the same length as nums1
    :return: the number of times two values at the same index are within 2 of each other
    """

    # Initialize a counter for the number of times two numbers are within 2 of each other
    differ_by_2 = 0

    # Using a loop to go through each index of the list
    for i in range(len(nums1)):

        # checking if both numbers at the same index in the two lists is within 2 of each other
        if 0 < abs(nums1[i] - nums2[i]) < 2:
            differ_by_2 += 1

    # Returning the counter
    return differ_by_2

def loudVowels(sentence):
    """
    takes a sentence and capitalizes all vowels
    :param sentence: a string of words
    :return: a string with all vowels capitalized
    """

    # Initialize a list of vowels and a list of the given string separated into letters
    vowels = ['a', 'e', 'i', 'o', 'u']
    sentence_list = list(sentence)

    # Using a loop to go through each letter, checking if its a vowel, and capitalizing if it is
    for i in range(len(sentence_list)):
        if sentence_list[i] in vowels:
            sentence_list[i] = sentence_list[i].upper()

    # Returning the string with capitalized vowels
    return "".join(sentence_list)

def diagonal(n):
    """
    Given a side length, print a grid with a diagonal line of 1's through the middle, 0's above the line, and 2's
    below the line
    :param n: a positive integer
    :return: none
    """

    # Initialize a grid of length and width n filled with 1's
    grid = []
    for i in range(n):
        grid.append([1]*n)

    # Formatting the grid with 0's above the minor diagonal and 2's below the diagonal
    for i in range(n):
        for j in range(n):
            if i + j < n - 1:
                grid[i][j] = 0
            elif i + j > n - 1:
                grid[i][j] = 2

        # Printing the formatted grind line by line
        print(" ".join([str(x) for x in grid[i]]))

print(two23([2, 2]))
print(after4([2, 4, 1, 2]))
print(closeby2([1, 2, 3], [2, 3, 10]))
print(loudVowels("I snap my fingers when I sing"))
diagonal(8)
hi



