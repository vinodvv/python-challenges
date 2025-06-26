"""
Day 21: List of Tuples
Write a function called make_tuples that takes two lists, equal lists,
and combines them into a list of tuples.

For example if list a is
[1,2,3,4] and list b is [5,6,7,8], your function should return
[(1,5),(2,6),(3,7),(4,8)].
"""


def make_tuples(lst1, lst2):
    result = zip(lst1, lst2)
    return list(tuple(result))


if __name__ == "__main__":
    print(make_tuples([1, 2, 3, 4], [5, 6, 7, 8]))


def make_tuples(lst1, lst2):
    tuples = []
    for i in range(len(lst1)):
        tuples.append((lst1[i], lst2[i]))
    return tuples


if __name__ == "__main__":
    print(make_tuples([5, 6, 7, 8], [1, 2, 3, 4],))
