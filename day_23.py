"""
Day 23: Simple Calculator

Create a simple calculator. The calculator should be able to perform basic
math operations, add, subtract, divide and multiply. The calculator
should take input from users. The calculator should be able to handle
ZeroDivisionError, NameError, and ValueError.
"""

import operator


def calculator():
    try:
        num1 = int(input("Enter number: "))
        # asking the user to pick an operator
        opt = input("Pick operator (+, -, *, /): ")
        num2 = int(input("Enter another number: "))

        if opt not in ['+', '-', '*', '/'] or len(opt) > 1:
            print("Please enter a valid operator.")

        # Handling zero division
        if opt == '/' and num2 == 0:
            return "You cannot divide a number by zero. Try again."

        # operator lookup using dictionary
        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        result = operations[opt](num1, num2)

    except ValueError:
        return "Please enter a valid number."
    except NameError:
        return "An unexpected error occurred (NameError)."


print(calculator())
