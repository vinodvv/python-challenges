"""
Day 3: Register Check

Write a function called register_check that checks how many students are in school.
The function takes a dictionary as a parameter. If the student is in school, the dictionary says ‘yes’.
If the student is not in school, the dictionary says ‘no’. Your function should return the number
of students in school.

Use the dictionary below. Your function should return 3.

register = {'Michael':'yes','John': 'no', 'Peter':'yes', 'Mary': 'yes'}

"""

register = {'Michael': 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'yes'}


def register_check(dictionary):
    count = 0
    for key, value in dictionary.items():
        if value == "yes":
            count += 1
    return f"Number of students is {count}."


if __name__ == "__main__":
    print(register_check(register))
