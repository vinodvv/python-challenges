"""
Write a Python program that counts how many numbers from 1 to 100 are divisible by both 3 and 5,
and also prints out exactly which numbers these are.

This is a classic small program that teaches you how to use:

- Loops (to go through each number in a range)

- The modulus operator % (to check for divisibility)

- Lists (to store matching numbers)

- And len() (to count the total)
"""


def divisible_by_3_and_5(start, end):
    numbers = [num for num in range(start, end + 1) if num % 3 == 0 and num % 5 == 0]
    return numbers, len(numbers)


try:
    user_start = int(input("Enter the starting number: "))
    user_end = int(input("Enter the ending number: "))
    result_numbers, result_count = divisible_by_3_and_5(user_start, user_end)
    print(f"\nNumbers from {user_start} to {user_end} divisible by both 3 and 5:")
    print(result_numbers)
    print(f"Total count: {result_count}")
except ValueError:
    print("Invalid input, Please enter valid numbers.")
except Exception as e:
    print(f"An error occurred: {e}")
