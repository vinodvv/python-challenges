"""
Day 2: Strings to Integers

Write a function called convert_add that takes a list of strings as an
argument and converts it to integers and sums the list.

For example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and summed to 9.
"""


def convert_add(list_of_strings):
    list_of_integers = []
    for string in list_of_strings:
        list_of_integers.append(int(string))
    return sum(list_of_integers)


print(convert_add(['1', '3', '5']))
