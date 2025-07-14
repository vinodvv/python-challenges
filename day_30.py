"""
Day 30: Most Repeated Name
Write a function called repeated_name that finds the most repeated
name in the following list.
name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
"""


def repeated_name(name_list):
    name_count = {}
    for name in name_list:
        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] = 1

    most_repeated = None
    max_count = 0

    for name, count in name_count.items():
        if count > max_count:
            max_count = count
            most_repeated = name
    return most_repeated


if __name__ == "__main__":
    name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
    result = repeated_name(name)
    print(f"The most repeated name is: {result}")
