"""
Day 22: Add Under_Score

Create three functions.

The first called add_hash takes a string and adds a hash # between the words.

The second function called add_underscore removes the hash(#) and replaces it with an underscore ( _ )

The third function called remove_underscore, removes the underscore and replaces it with nothing.

if you pass ‘Python’ as an argument for the three functions, and you call them at the same time as:

print(remove_underscore(add_underscore(add_hash('Python')))) it should return ‘Python’.
"""


def add_hash(string):
    return "#".join(string)


def add_underscore(string):
    return str(string).replace("#", "_")


def remove_underscore(string):
    return str(string).replace("_", "")


if __name__ == "__main__":
    # print(add_hash("Python"))
    # print(add_underscore(add_hash("Python")))
    # print(remove_underscore(add_underscore("Python")))
    print(remove_underscore(add_underscore(add_hash("Python"))))
