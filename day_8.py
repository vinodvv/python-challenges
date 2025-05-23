"""
Day 8: Odd and Even

Write a function called odd_even that has one parameter and takes a list of numbers as an argument. The function
returns the difference between the largest even number in the list and the smallest odd number in the list.

For example, if you pass [1,2,4,6] as an argument the function should return 6 - 1= 5.
"""


def odd_even(num):
    odd_numbers = [num for num in num if num % 2 != 0]
    even_numbers = [num for num in num if num % 2 == 0]
    difference = max(even_numbers) - min(odd_numbers)
    return f"The difference between largest even number and smallest odd number is {difference}."


if __name__ == "__main__":
    print(odd_even([1, 2, 4, 6]))
