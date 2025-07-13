"""
Day 28: Return Indexes
Write a function called index_position. This function takes a string
as a parameter and returns the positions or indexes of all lower
letters in the string. For example ‘LovE’ should return [1,2].
"""


def index_position(string):
    index_position = []
    for index, char in enumerate(string):  # Get both index and character while iterating
        if char.islower():  # Checks if each character is lowercase
            index_position.append(index)  # Appends to index_position list
    return index_position  # returns list


def index_posn(string):
    indexes = [index for index, char in enumerate(string) if char.islower()]
    return indexes


if __name__ == "__main__":
    print(index_position("LovE"))
    print(index_posn("LovE"))
