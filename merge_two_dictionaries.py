"""
Python Challenge: Merge Two Dictionaries

Write a Python program that merges two dictionaries into a new one.

The program should:
    * Start with two predefined dictionaries (hardcode them)
    * Merge them into a new dictionary
    * Print out the result

This is a great opportunity to practice both the modern unpacking method and the more traditional update method. Try both!
"""


# Solution 1
def merged_dicts(a, b):
    merged = {**a, **b}
    return merged


# Solution 2
def merged_dictionaries(a, b):
    merged = a.copy()
    merged.update(b)
    return merged


if __name__ == "__main__":
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}

    merged_dict = merged_dicts(dict1, dict2)
    merged_dict2 = merged_dictionaries(dict1, dict2)
    print(f"Merged dictionary using Solution 1: {merged_dict}\n")
    print(f"Merged dictionary using Solution 2: {merged_dict2}")
