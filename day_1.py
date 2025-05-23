"""
Day 1: Division and Square-root
Write a function called divide_or_square that takes one argument (a number),
and returns the square root of the number if it is divisible by 5,
returns its remainder if it is not divisible by 5.

For example, if you pass 10 as an argument,
then your function should return 3.16 as the square root.
"""


def divide_or_square(number):
    if number % 5 == 0:
        square_root = number ** 0.5
        return f"The square root of the number is {round(square_root, 2)}."
    else:
        reminder = number % 5
        return f"The reminder of division is {round(reminder, 2)}."


if __name__ == "__main__":
    print(divide_or_square(10))
