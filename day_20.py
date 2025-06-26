"""
Day 20: Capitalize First Letter
Write a function called capitalize. This function takes a string as an argument and capitalizes the first letter of each word.

For example, ‘i like learning’ becomes ‘I Like Learning’.
"""


def capitalize(string):
    upper = []
    for i, word in enumerate(string.split()):
        if word[0].islower():
            upper.append(word.capitalize())
        else:
            upper.append(word)
    return " ".join(upper)


def capital(string):
    string = string.title()
    return string


if __name__ == "__main__":
    print(capitalize("i like learning"))
    print(capital("i like learning"))
