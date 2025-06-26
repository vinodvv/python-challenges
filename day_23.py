"""
Day 23: Simple Calculator

Create a simple calculator. The calculator should be able to perform basic
math operations, add, subtract, divide and multiply. The calculator
should take input from users. The calculator should be able to handle
ZeroDivisionError, NameError, and ValueError.
"""

import operator


def calculator():
    while True:
        try:
            num1 = float(input("Enter number: "))
            # asking the user to pick an operator
            opt = input("Pick operator (+, -, *, /): ")
            num2 = float(input("Enter another number: "))

            if opt not in ['+', '-', '*', '/'] or len(opt) > 1:
                print("Please enter a valid operator.")
                continue

            # Handling zero division
            if opt == '/' and num2 == 0:
                print("You cannot divide a number by zero. Try again.")
                continue

            # operator lookup using dictionary
            operations = {
                '+': operator.add,
                '-': operator.sub,
                '*': operator.mul,
                '/': operator.truediv
            }

            result = operations[opt](num1, num2)
            print(f"\nans is: {result}.")

        except ValueError:
            print("Please enter a valid number.")
        except NameError:
            print("An unexpected error occurred (NameError).")

        # Ask user if they want to continue
        again = input("Do you want to perform another calculation? (y/n): ").lower()
        if again != 'y':
            print("Thanks for using the calculator. Goodbye!")
            break


if __name__ == "__main__":
    # Start calculator
    calculator()
