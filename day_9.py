"""
Day 9: Biggest Odd Number

Create a function called biggest_odd that takes a string of numbers
and returns the biggest odd number in the list.

For example, if you pass ‘23569’ as an argument, your function should return 9.
Use list comprehension.
"""


def biggest_odd(string):
    odd_numbers = [string for string in string if int(string) % 2 != 0]
    return f"Biggest odd number is {max(odd_numbers)}."


def biggest_even(list_of_string):
    list_of_numbers = [int(string) for string in list_of_string]
    even_numbers = [num for num in list_of_numbers if num % 2 == 0]
    return f"Biggest even number is {max(even_numbers)}."


def smallest_odd(list_of_string):
    odd_numbers = [string for string in list_of_string if int(string) % 2 != 0]
    return f"Smallest odd number is {min(odd_numbers)}."


def smallest_even(list_of_string):
    even_numbers = [string for string in list_of_string if int(string) % 2 == 0]
    return f"Smallest even number is {min(even_numbers)}."


if __name__ == "__main__":
    print(biggest_odd('23569'))
    print(biggest_even('23569'))
    print(smallest_odd('23569'))
    print(smallest_even('23569'))
