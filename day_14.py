"""
Day 14: Flatten the List

Write a function called flat_list that takes one argument, a nested
list. The function converts the nested list into a one-dimension list.

For example [[2,4,5,6]] should return [2,4,5,6].
"""


def flat_list(nested_list):
    flattened_list = []
    for sublist in nested_list:
        for item in sublist:
            flattened_list.append(item)
    return flattened_list


if __name__ == "__main__":
    print(flat_list([[2, 4, 5, 6]]))
    print(flat_list([[2 ,3, 4, 5, 6], [3, 5, 7, 9]]))
