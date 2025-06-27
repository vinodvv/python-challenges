"""
Create a function called average_calories that calculates the average
calories intake of a user. The function should ask the user to input their
calories intake for any number of days and once they hit ‘done’ it
should calculate and return the average intake.
"""


def average_calories():
    scores = []
    while True:
        score = input("Enter a score or 'done' to quit: ")
        if score.lower() == 'done':
            break
        try:
            scores.append(int(score))
        except ValueError:
            print("Please enter a valid integer or 'done'.")

    if not scores:
        return "No scores entered. Cannot compute average."

    return f"Mean of scores is {sum(scores) / len(scores):.2f}"


if __name__ == "__main__":
    print(average_calories())
