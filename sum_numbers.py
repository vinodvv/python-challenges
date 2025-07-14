def sum_all_numbers(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num
    return f"The sum of all numbers from {start} to {end} is: {total}"


def get_integer_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.lower() == "exit":
            return "exit"
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer or type 'exit' to quit.")


if __name__ == "__main__":
    print("Welcome to the Range Sum Calculator!")
    print("You can type 'exit' anytime to quit.\n")

    while True:
        start = get_integer_input("Enter the start of the range: ")
        if start == "exit":
            print("Goodbye!")
            break

        end = get_integer_input("Enter the end of the range: ")
        if end == "exit":
            print("Goodbye!")
            break

        if start > end:
            print(f"Note: Start ({start}) is greater than end ({end}). Swapping values.")
            start, end = end, start

        result = sum_all_numbers(start, end)
        print(result)
        print("-" * 40)
