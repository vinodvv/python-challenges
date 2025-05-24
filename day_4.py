"""
Day 4: Only Floats

Write a function called only_floats, which takes two parameters a and b,
and returns 2 if both arguments are floats, returns 1 if only
one argument is a float, and returns 0 if neither argument is a float.

If you pass (12.1, 23) as an argument, your function should return a 1.
"""


def only_floats(a, b):
    if isinstance(a, float) and isinstance(b, float):
        return 2
    elif isinstance(a, float) or isinstance(b, float):
        return 1
    else:
        return 0


def floats(a, b):
    match (isinstance(a, float), isinstance(b, float)):
        case(True, True):
            return 2
        case (True, False) | (False, True):
            return 1
        case (False, False):
            return 0


if __name__ == "__main__":
    print(only_floats(12.1, 23))
    print(floats(23, 12.2))
