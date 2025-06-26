"""
Day 19: Words and Elements

Write two functions. The first function is called count_words which
takes a string of words and counts how many words are in the string.
The second function called count_elements takes a string of words
and counts how many elements are in the string. Do not count the
whitespaces. The first function will return the number of words in a
string and the second one will return the number of elements (less
whitespace).

If you pass ‘I love learning’, the count_words function
should return 3 words and count_elements should return 13
elements.
"""


# def count_words(string):
#     string = string.split()
#     count = len(string)
#     return f"{count} words."


def count_words(string):
    words = []
    for i in string.split():
        words.append(i)
    return f"There are {len(words)} words in the sentence."


# def count_elements(string):
#     string = string.split()
#     elements = 0
#     for word in string:
#         for _ in word:
#             elements += 1
#     return elements


def count_elements(string):
    string = string.replace(" ", "")
    return f"The string has {len(string)} elements."


if __name__ == "__main__":
    print(count_words("I love learning"))
    print(count_elements("I love learning"))
