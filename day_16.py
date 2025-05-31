"""
Day 16: Sum the List

Write a function called sum_list with one parameter that takes a
nested list of integers as an argument and returns the sum of the
integers.

For example, if you pass [[2, 4, 5, 6], [2, 3, 5, 6]] as an
argument your function should return a sum of 33.
"""


def sum_list(nested_list):
    result = 0
    for sublist in nested_list:
        for item in sublist:
            result += item
    return f"The sum is {result}"


if __name__ == "__main__":
    print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]))
