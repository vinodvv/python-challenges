"""
Day 8: Odd and Even

Write a function called odd_even that has one parameter and takes a list of numbers as an argument. The function
returns the difference between the largest even number in the list and the smallest odd number in the list.

For example, if you pass [1,2,4,6] as an argument the function should return 6 - 1= 5.
"""


def even_odd(numbers):
    odd_numbers = []
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    largest_even_number = max(even_numbers)
    smallest_odd_number = min(odd_numbers)
    return largest_even_number - smallest_odd_number


def find_odd_even(numbers):
    odd = []
    even = []
    for num in numbers:
        match (num % 2 == 0):
            case True:
                even.append(num)
            case False:
                odd.append(num)
    difference = max(even) - min(odd)
    return difference


# Using list comprehension
def odd_even(num):
    odd_numbers = [num for num in num if num % 2 != 0]
    even_numbers = [num for num in num if num % 2 == 0]
    difference = max(even_numbers) - min(odd_numbers)
    return f"The difference between largest even number and smallest odd number is {difference}."


if __name__ == "__main__":
    print(even_odd([1, 2, 4, 6]))
    print(odd_even([1, 2, 4, 6]))
    print(find_odd_even([5, 7, 4, 6, 8]))