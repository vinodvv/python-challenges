"""
Build a Python program that calculates the sum of all numbers in a user-defined range.
Instead of hardcoding the start and end values, your program will prompt the user to enter them.
You’ll then write a function that loops through each number from the start to the end (inclusive)
and calculates the total sum.
"""


def sum_all_numbers(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num
    return f"The sum of all numbers from {start} to {end} is: {total}"


if __name__ == "__main__":
    try:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        if start > end:
            print(f"Note: Start of the range ({start}) is greater than end of the range ({end}). Swapping values.")
            start, end = end, start  # Swap to ensure a valid range
            result = sum_all_numbers(start, end)
            print(result)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")
